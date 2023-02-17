
# Results vs. base

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: b560583
- commit date: 2023-02-17
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230217-linux-x86_64-python-072011b3c38f871cdc3a-3.12.0a5+-072011b | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 248 ms                                                                 | 246 ms: 1.01x faster                                                   |
| chameleon      | 6.50 ms                                                                | 6.29 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230217-linux-x86_64-python-072011b3c38f871cdc3a-3.12.0a5+-072011b | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 74.8 ms                                                                | 72.5 ms: 1.03x faster                                                  |
| pidigits       | 193 ms                                                                 | 189 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230217-linux-x86_64-python-072011b3c38f871cdc3a-3.12.0a5+-072011b | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                                | 21.3 ms: 1.03x faster                                                  |
| regex_effbot   | 3.31 ms                                                                | 3.28 ms: 1.01x faster                                                  |
| regex_compile  | 130 ms                                                                 | 129 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230217-linux-x86_64-python-072011b3c38f871cdc3a-3.12.0a5+-072011b | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 9.60 ms                                                                | 9.33 ms: 1.03x faster                                                  |
| json_loads           | 24.0 us                                                                | 23.5 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 102 ms                                                                 | 100 ms: 1.02x faster                                                   |
| xml_etree_generate   | 81.9 ms                                                                | 80.7 ms: 1.01x faster                                                  |
| unpickle_pure_python | 198 us                                                                 | 196 us: 1.01x faster                                                   |
| pickle_pure_python   | 284 us                                                                 | 281 us: 1.01x faster                                                   |
| xml_etree_process    | 56.4 ms                                                                | 56.2 ms: 1.00x faster                                                  |
| pickle               | 10.2 us                                                                | 10.3 us: 1.01x slower                                                  |
| unpickle_list        | 4.98 us                                                                | 5.08 us: 1.02x slower                                                  |
| pickle_dict          | 30.7 us                                                                | 31.4 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (3): unpickle, xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230217-linux-x86_64-python-072011b3c38f871cdc3a-3.12.0a5+-072011b | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.55 ms                                                                | 6.50 ms: 1.01x faster                                                  |
| python_startup         | 9.04 ms                                                                | 8.97 ms: 1.01x faster                                                  |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230217-linux-x86_64-python-072011b3c38f871cdc3a-3.12.0a5+-072011b | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text    | 21.1 ms                                                                | 20.9 ms: 1.01x faster                                                  |
| mako           | 9.85 ms                                                                | 9.89 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230217-linux-x86_64-python-072011b3c38f871cdc3a-3.12.0a5+-072011b | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal            | 3.83 ms                                                                | 3.53 ms: 1.09x faster                                                  |
| unpack_sequence         | 43.7 ns                                                                | 41.3 ns: 1.06x faster                                                  |
| richards                | 44.6 ms                                                                | 42.4 ms: 1.05x faster                                                  |
| go                      | 140 ms                                                                 | 134 ms: 1.05x faster                                                   |
| nqueens                 | 81.1 ms                                                                | 77.6 ms: 1.05x faster                                                  |
| scimark_sparse_mat_mult | 4.26 ms                                                                | 4.08 ms: 1.04x faster                                                  |
| spectral_norm           | 96.7 ms                                                                | 92.9 ms: 1.04x faster                                                  |
| pprint_safe_repr        | 692 ms                                                                 | 670 ms: 1.03x faster                                                   |
| chameleon               | 6.50 ms                                                                | 6.29 ms: 1.03x faster                                                  |
| regex_v8                | 22.0 ms                                                                | 21.3 ms: 1.03x faster                                                  |
| float                   | 74.8 ms                                                                | 72.5 ms: 1.03x faster                                                  |
| pprint_pformat          | 1.43 sec                                                               | 1.38 sec: 1.03x faster                                                 |
| scimark_monte_carlo     | 66.7 ms                                                                | 64.7 ms: 1.03x faster                                                  |
| deepcopy_reduce         | 3.01 us                                                                | 2.93 us: 1.03x faster                                                  |
| json_dumps              | 9.60 ms                                                                | 9.33 ms: 1.03x faster                                                  |
| dask                    | 512 ms                                                                 | 499 ms: 1.03x faster                                                   |
| coroutines              | 23.2 ms                                                                | 22.7 ms: 1.02x faster                                                  |
| create_gc_cycles        | 1.51 ms                                                                | 1.47 ms: 1.02x faster                                                  |
| async_generators        | 421 ms                                                                 | 412 ms: 1.02x faster                                                   |
| coverage                | 98.3 ms                                                                | 96.4 ms: 1.02x faster                                                  |
| scimark_lu              | 111 ms                                                                 | 109 ms: 1.02x faster                                                   |
| logging_silent          | 93.9 ns                                                                | 92.1 ns: 1.02x faster                                                  |
| json_loads              | 24.0 us                                                                | 23.5 us: 1.02x faster                                                  |
| scimark_fft             | 311 ms                                                                 | 306 ms: 1.02x faster                                                   |
| crypto_pyaes            | 73.9 ms                                                                | 72.6 ms: 1.02x faster                                                  |
| xml_etree_iterparse     | 102 ms                                                                 | 100 ms: 1.02x faster                                                   |
| pidigits                | 193 ms                                                                 | 189 ms: 1.02x faster                                                   |
| sympy_expand            | 462 ms                                                                 | 455 ms: 1.02x faster                                                   |
| xml_etree_generate      | 81.9 ms                                                                | 80.7 ms: 1.01x faster                                                  |
| deepcopy_memo           | 34.8 us                                                                | 34.3 us: 1.01x faster                                                  |
| unpickle_pure_python    | 198 us                                                                 | 196 us: 1.01x faster                                                   |
| bench_thread_pool       | 795 us                                                                 | 785 us: 1.01x faster                                                   |
| gunicorn                | 1.09 ms                                                                | 1.08 ms: 1.01x faster                                                  |
| sqlglot_normalize       | 105 ms                                                                 | 104 ms: 1.01x faster                                                   |
| pickle_pure_python      | 284 us                                                                 | 281 us: 1.01x faster                                                   |
| hexiom                  | 6.16 ms                                                                | 6.10 ms: 1.01x faster                                                  |
| sqlglot_optimize        | 51.3 ms                                                                | 50.8 ms: 1.01x faster                                                  |
| asyncio_tcp             | 506 ms                                                                 | 501 ms: 1.01x faster                                                   |
| regex_effbot            | 3.31 ms                                                                | 3.28 ms: 1.01x faster                                                  |
| genshi_text             | 21.1 ms                                                                | 20.9 ms: 1.01x faster                                                  |
| pycparser               | 1.11 sec                                                               | 1.10 sec: 1.01x faster                                                 |
| mypy2                   | 332 ms                                                                 | 329 ms: 1.01x faster                                                   |
| dulwich_log             | 63.2 ms                                                                | 62.6 ms: 1.01x faster                                                  |
| sympy_sum               | 160 ms                                                                 | 158 ms: 1.01x faster                                                   |
| thrift                  | 766 us                                                                 | 759 us: 1.01x faster                                                   |
| aiohttp                 | 1.01 ms                                                                | 1.00 ms: 1.01x faster                                                  |
| sqlglot_parse           | 1.44 ms                                                                | 1.43 ms: 1.01x faster                                                  |
| sympy_str               | 274 ms                                                                 | 272 ms: 1.01x faster                                                   |
| mdp                     | 2.64 sec                                                               | 2.62 sec: 1.01x faster                                                 |
| python_startup_no_site  | 6.55 ms                                                                | 6.50 ms: 1.01x faster                                                  |
| python_startup          | 9.04 ms                                                                | 8.97 ms: 1.01x faster                                                  |
| 2to3                    | 248 ms                                                                 | 246 ms: 1.01x faster                                                   |
| sqlglot_transpile       | 1.73 ms                                                                | 1.72 ms: 1.01x faster                                                  |
| regex_compile           | 130 ms                                                                 | 129 ms: 1.01x faster                                                   |
| xml_etree_process       | 56.4 ms                                                                | 56.2 ms: 1.00x faster                                                  |
| sympy_integrate         | 20.0 ms                                                                | 19.9 ms: 1.00x faster                                                  |
| pyflate                 | 407 ms                                                                 | 408 ms: 1.00x slower                                                   |
| mako                    | 9.85 ms                                                                | 9.89 ms: 1.00x slower                                                  |
| logging_simple          | 5.69 us                                                                | 5.73 us: 1.01x slower                                                  |
| fannkuch                | 364 ms                                                                 | 366 ms: 1.01x slower                                                   |
| logging_format          | 6.29 us                                                                | 6.34 us: 1.01x slower                                                  |
| deepcopy                | 332 us                                                                 | 335 us: 1.01x slower                                                   |
| pickle                  | 10.2 us                                                                | 10.3 us: 1.01x slower                                                  |
| pathlib                 | 18.1 ms                                                                | 18.4 ms: 1.02x slower                                                  |
| unpickle_list           | 4.98 us                                                                | 5.08 us: 1.02x slower                                                  |
| generators              | 30.6 ms                                                                | 31.3 ms: 1.02x slower                                                  |
| pickle_dict             | 30.7 us                                                                | 31.4 us: 1.02x slower                                                  |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (26): unpickle, async_tree_cpu_io_mixed, async_tree_memoization, sqlalchemy_imperative, json, scimark_sor, django_template, sqlite_synth, sqlalchemy_declarative, tornado_http, chaos, telco, djangocms, xml_etree_parse, bench_mp_pool, pickle_list, async_tree_io, async_tree_none, genshi_xml, regex_dna, docutils, raytrace, nbody, deltablue, meteor_contest, html5lib
