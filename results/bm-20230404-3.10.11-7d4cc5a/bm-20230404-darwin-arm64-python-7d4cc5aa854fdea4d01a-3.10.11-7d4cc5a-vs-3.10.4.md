
# Results vs. 3.10.4

- fork: python
- ref: 7d4cc5aa854fdea4d01a
- machine: darwin-arm64
- commit hash: 7d4cc5a
- commit date: 2023-04-04
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 203 ms: 1.01x slower                                                 |
| chameleon      | 5.79 ms                                                | 5.75 ms: 1.01x faster                                                |
| docutils       | 1.78 sec                                               | 1.79 sec: 1.01x slower                                               |
| html5lib       | 44.2 ms                                                | 47.8 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x slower                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 72.2 ms: 1.00x faster                                                |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                 |
| nbody          | 93.3 ms                                                | 94.0 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 96.9 ms: 1.01x slower                                                |
| regex_v8       | 17.6 ms                                                | 18.0 ms: 1.02x slower                                                |
| regex_effbot   | 2.46 ms                                                | 2.69 ms: 1.10x slower                                                |
| regex_dna      | 162 ms                                                 | 185 ms: 1.14x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|---------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps          | 8.40 ms                                                | 8.27 ms: 1.02x faster                                                |
| xml_etree_process   | 44.8 ms                                                | 44.9 ms: 1.00x slower                                                |
| xml_etree_generate  | 54.2 ms                                                | 54.3 ms: 1.00x slower                                                |
| pickle_pure_python  | 283 us                                                 | 285 us: 1.01x slower                                                 |
| xml_etree_iterparse | 72.3 ms                                                | 73.2 ms: 1.01x slower                                                |
| pickle              | 7.35 us                                                | 7.56 us: 1.03x slower                                                |
| pickle_list         | 2.80 us                                                | 2.90 us: 1.03x slower                                                |
| pickle_dict         | 17.9 us                                                | 18.8 us: 1.05x slower                                                |
| Geometric mean      | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (5): json_loads, unpickle, unpickle_pure_python, unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.1 ms: 1.02x slower                                                |
| python_startup_no_site | 8.88 ms                                                | 9.13 ms: 1.03x slower                                                |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 18.4 ms                                                | 18.2 ms: 1.01x faster                                                |
| django_template | 27.3 ms                                                | 27.1 ms: 1.01x faster                                                |
| genshi_xml      | 37.2 ms                                                | 37.3 ms: 1.00x slower                                                |
| mako            | 10.5 ms                                                | 10.6 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                         |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| dask                    | 265 ms                                                 | 257 ms: 1.03x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.33 ms: 1.03x faster                                                |
| sqlglot_transpile       | 1.57 ms                                                | 1.53 ms: 1.03x faster                                                |
| bench_thread_pool       | 546 us                                                 | 532 us: 1.03x faster                                                 |
| pathlib                 | 28.8 ms                                                | 28.3 ms: 1.02x faster                                                |
| json_dumps              | 8.40 ms                                                | 8.27 ms: 1.02x faster                                                |
| richards                | 51.4 ms                                                | 50.7 ms: 1.01x faster                                                |
| deepcopy                | 281 us                                                 | 279 us: 1.01x faster                                                 |
| genshi_text             | 18.4 ms                                                | 18.2 ms: 1.01x faster                                                |
| json                    | 3.08 ms                                                | 3.06 ms: 1.01x faster                                                |
| chameleon               | 5.79 ms                                                | 5.75 ms: 1.01x faster                                                |
| pprint_safe_repr        | 606 ms                                                 | 602 ms: 1.01x faster                                                 |
| create_gc_cycles        | 880 us                                                 | 874 us: 1.01x faster                                                 |
| django_template         | 27.3 ms                                                | 27.1 ms: 1.01x faster                                                |
| coverage                | 42.0 ms                                                | 41.9 ms: 1.00x faster                                                |
| async_generators        | 234 ms                                                 | 233 ms: 1.00x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 36.9 ms: 1.00x faster                                                |
| go                      | 165 ms                                                 | 165 ms: 1.00x faster                                                 |
| float                   | 72.4 ms                                                | 72.2 ms: 1.00x faster                                                |
| nqueens                 | 68.2 ms                                                | 68.0 ms: 1.00x faster                                                |
| sqlglot_normalize       | 196 ms                                                 | 196 ms: 1.00x faster                                                 |
| pidigits                | 282 ms                                                 | 282 ms: 1.00x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 78.0 ms: 1.00x faster                                                |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.46 ms: 1.00x slower                                                |
| xml_etree_process       | 44.8 ms                                                | 44.9 ms: 1.00x slower                                                |
| crypto_pyaes            | 78.1 ms                                                | 78.3 ms: 1.00x slower                                                |
| mdp                     | 1.66 sec                                               | 1.67 sec: 1.00x slower                                               |
| scimark_fft             | 230 ms                                                 | 231 ms: 1.00x slower                                                 |
| xml_etree_generate      | 54.2 ms                                                | 54.3 ms: 1.00x slower                                                |
| genshi_xml              | 37.2 ms                                                | 37.3 ms: 1.00x slower                                                |
| fannkuch                | 317 ms                                                 | 319 ms: 1.00x slower                                                 |
| pyflate                 | 453 ms                                                 | 455 ms: 1.00x slower                                                 |
| scimark_lu              | 109 ms                                                 | 110 ms: 1.00x slower                                                 |
| sympy_expand            | 275 ms                                                 | 277 ms: 1.00x slower                                                 |
| logging_simple          | 4.63 us                                                | 4.65 us: 1.01x slower                                                |
| spectral_norm           | 95.8 ms                                                | 96.4 ms: 1.01x slower                                                |
| regex_compile           | 96.4 ms                                                | 96.9 ms: 1.01x slower                                                |
| deltablue               | 5.14 ms                                                | 5.17 ms: 1.01x slower                                                |
| pickle_pure_python      | 283 us                                                 | 285 us: 1.01x slower                                                 |
| docutils                | 1.78 sec                                               | 1.79 sec: 1.01x slower                                               |
| nbody                   | 93.3 ms                                                | 94.0 ms: 1.01x slower                                                |
| sympy_integrate         | 13.3 ms                                                | 13.4 ms: 1.01x slower                                                |
| sympy_str               | 169 ms                                                 | 170 ms: 1.01x slower                                                 |
| 2to3                    | 201 ms                                                 | 203 ms: 1.01x slower                                                 |
| mako                    | 10.5 ms                                                | 10.6 ms: 1.01x slower                                                |
| bench_mp_pool           | 39.7 ms                                                | 40.2 ms: 1.01x slower                                                |
| xml_etree_iterparse     | 72.3 ms                                                | 73.2 ms: 1.01x slower                                                |
| sqlalchemy_imperative   | 8.89 ms                                                | 9.01 ms: 1.01x slower                                                |
| comprehensions          | 17.6 us                                                | 17.9 us: 1.02x slower                                                |
| logging_format          | 4.97 us                                                | 5.05 us: 1.02x slower                                                |
| raytrace                | 325 ms                                                 | 331 ms: 1.02x slower                                                 |
| python_startup          | 11.9 ms                                                | 12.1 ms: 1.02x slower                                                |
| chaos                   | 66.7 ms                                                | 68.0 ms: 1.02x slower                                                |
| regex_v8                | 17.6 ms                                                | 18.0 ms: 1.02x slower                                                |
| unpack_sequence         | 37.4 ns                                                | 38.3 ns: 1.02x slower                                                |
| pickle                  | 7.35 us                                                | 7.56 us: 1.03x slower                                                |
| python_startup_no_site  | 8.88 ms                                                | 9.13 ms: 1.03x slower                                                |
| sympy_sum               | 93.6 ms                                                | 96.4 ms: 1.03x slower                                                |
| pickle_list             | 2.80 us                                                | 2.90 us: 1.03x slower                                                |
| pickle_dict             | 17.9 us                                                | 18.8 us: 1.05x slower                                                |
| html5lib                | 44.2 ms                                                | 47.8 ms: 1.08x slower                                                |
| regex_effbot            | 2.46 ms                                                | 2.69 ms: 1.10x slower                                                |
| regex_dna               | 162 ms                                                 | 185 ms: 1.14x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (32): aiohttp, pycparser, gunicorn, async_tree_none, tornado_http, scimark_monte_carlo, json_loads, async_tree_cpu_io_mixed, async_tree_io, asyncio_tcp, telco, async_tree_memoization, generators, thrift, coroutines, pprint_pformat, scimark_sor, gc_traversal, pylint, sqlglot_optimize, unpickle, sqlalchemy_declarative, logging_silent, deepcopy_memo, deepcopy_reduce, sqlite_synth, unpickle_pure_python, hexiom, mypy2, unpickle_list, flaskblogging, xml_etree_parse
