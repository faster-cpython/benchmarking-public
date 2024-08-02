
# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a2
- machine: darwin-arm64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 179 ms: 1.07x faster                                       |
| chameleon      | 6.26 ms                                                | 4.93 ms: 1.27x faster                                      |
| docutils       | 1.73 sec                                               | 1.51 sec: 1.15x faster                                     |
| tornado_http   | 86.7 ms                                                | 71.4 ms: 1.21x faster                                      |
| Geometric mean | (ref)                                                  | 1.17x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 263 ms: 1.48x faster                                       |
| async_tree_memoization  | 474 ms                                                 | 339 ms: 1.40x faster                                       |
| async_tree_io           | 980 ms                                                 | 719 ms: 1.36x faster                                       |
| async_tree_cpu_io_mixed | 649 ms                                                 | 532 ms: 1.22x faster                                       |
| Geometric mean          | (ref)                                                  | 1.36x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 86.3 ms: 1.08x faster                                      |
| float          | 69.0 ms                                                | 68.2 ms: 1.01x faster                                      |
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 155 ms: 1.12x faster                                       |
| regex_compile  | 95.3 ms                                                | 85.5 ms: 1.11x faster                                      |
| regex_v8       | 17.1 ms                                                | 17.4 ms: 1.01x slower                                      |
| regex_effbot   | 2.46 ms                                                | 2.56 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 201 us: 1.40x faster                                       |
| json_dumps           | 8.11 ms                                                | 6.61 ms: 1.23x faster                                      |
| unpickle_pure_python | 194 us                                                 | 168 us: 1.16x faster                                       |
| xml_etree_process    | 46.5 ms                                                | 41.2 ms: 1.13x faster                                      |
| tomli_loads          | 1.71 sec                                               | 1.67 sec: 1.02x faster                                     |
| unpickle             | 8.80 us                                                | 8.99 us: 1.02x slower                                      |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                      |
| pickle               | 6.97 us                                                | 7.36 us: 1.06x slower                                      |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.07x slower                                      |
| pickle_list          | 2.74 us                                                | 2.93 us: 1.07x slower                                      |
| unpickle_list        | 2.69 us                                                | 2.98 us: 1.11x slower                                      |
| xml_etree_generate   | 53.5 ms                                                | 59.6 ms: 1.11x slower                                      |
| xml_etree_iterparse  | 72.1 ms                                                | 81.1 ms: 1.12x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 12.7 ms: 1.16x slower                                      |
| python_startup_no_site | 7.91 ms                                                | 11.4 ms: 1.44x slower                                      |
| Geometric mean         | (ref)                                                  | 1.29x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 9.87 ms                                                | 9.60 ms: 1.03x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 77.1 us: 4.19x faster                                      |
| logging_silent           | 117 ns                                                 | 72.1 ns: 1.62x faster                                      |
| raytrace                 | 301 ms                                                 | 195 ms: 1.55x faster                                       |
| richards_super           | 57.8 ms                                                | 37.7 ms: 1.53x faster                                      |
| asyncio_tcp              | 659 ms                                                 | 435 ms: 1.52x faster                                       |
| sqlglot_parse            | 1.24 ms                                                | 838 us: 1.48x faster                                       |
| async_tree_none          | 388 ms                                                 | 263 ms: 1.48x faster                                       |
| richards                 | 48.7 ms                                                | 33.6 ms: 1.45x faster                                      |
| sqlglot_transpile        | 1.44 ms                                                | 1.02 ms: 1.42x faster                                      |
| pickle_pure_python       | 281 us                                                 | 201 us: 1.40x faster                                       |
| async_tree_memoization   | 474 ms                                                 | 339 ms: 1.40x faster                                       |
| chaos                    | 65.8 ms                                                | 47.5 ms: 1.39x faster                                      |
| unpack_sequence          | 39.0 ns                                                | 28.2 ns: 1.38x faster                                      |
| deltablue                | 4.91 ms                                                | 3.59 ms: 1.37x faster                                      |
| async_tree_io            | 980 ms                                                 | 719 ms: 1.36x faster                                       |
| scimark_lu               | 103 ms                                                 | 76.1 ms: 1.35x faster                                      |
| go                       | 151 ms                                                 | 112 ms: 1.35x faster                                       |
| crypto_pyaes             | 71.8 ms                                                | 54.5 ms: 1.32x faster                                      |
| deepcopy_memo            | 34.7 us                                                | 26.7 us: 1.30x faster                                      |
| chameleon                | 6.26 ms                                                | 4.93 ms: 1.27x faster                                      |
| pycparser                | 877 ms                                                 | 706 ms: 1.24x faster                                       |
| logging_format           | 4.83 us                                                | 3.90 us: 1.24x faster                                      |
| logging_simple           | 4.45 us                                                | 3.60 us: 1.24x faster                                      |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.30 sec: 1.23x faster                                     |
| json_dumps               | 8.11 ms                                                | 6.61 ms: 1.23x faster                                      |
| create_gc_cycles         | 860 us                                                 | 704 us: 1.22x faster                                       |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 532 ms: 1.22x faster                                       |
| tornado_http             | 86.7 ms                                                | 71.4 ms: 1.21x faster                                      |
| deepcopy                 | 272 us                                                 | 224 us: 1.21x faster                                       |
| scimark_sor              | 128 ms                                                 | 106 ms: 1.21x faster                                       |
| deepcopy_reduce          | 2.33 us                                                | 1.95 us: 1.19x faster                                      |
| dulwich_log              | 35.3 ms                                                | 30.1 ms: 1.18x faster                                      |
| unpickle_pure_python     | 194 us                                                 | 168 us: 1.16x faster                                       |
| generators               | 32.3 ms                                                | 28.0 ms: 1.16x faster                                      |
| pyflate                  | 427 ms                                                 | 369 ms: 1.16x faster                                       |
| sympy_sum                | 92.2 ms                                                | 80.2 ms: 1.15x faster                                      |
| docutils                 | 1.73 sec                                               | 1.51 sec: 1.15x faster                                     |
| mypy2                    | 607 ms                                                 | 532 ms: 1.14x faster                                       |
| pprint_safe_repr         | 641 ms                                                 | 561 ms: 1.14x faster                                       |
| scimark_monte_carlo      | 65.6 ms                                                | 57.9 ms: 1.13x faster                                      |
| pprint_pformat           | 1.30 sec                                               | 1.15 sec: 1.13x faster                                     |
| xml_etree_process        | 46.5 ms                                                | 41.2 ms: 1.13x faster                                      |
| regex_dna                | 174 ms                                                 | 155 ms: 1.12x faster                                       |
| sympy_integrate          | 13.1 ms                                                | 11.7 ms: 1.12x faster                                      |
| regex_compile            | 95.3 ms                                                | 85.5 ms: 1.11x faster                                      |
| coroutines               | 20.7 ms                                                | 18.6 ms: 1.11x faster                                      |
| sympy_str                | 165 ms                                                 | 149 ms: 1.11x faster                                       |
| sympy_expand             | 269 ms                                                 | 243 ms: 1.10x faster                                       |
| dask                     | 253 ms                                                 | 230 ms: 1.10x faster                                       |
| nbody                    | 93.0 ms                                                | 86.3 ms: 1.08x faster                                      |
| comprehensions           | 16.9 us                                                | 15.7 us: 1.08x faster                                      |
| 2to3                     | 192 ms                                                 | 179 ms: 1.07x faster                                       |
| json                     | 3.08 ms                                                | 2.99 ms: 1.03x faster                                      |
| mako                     | 9.87 ms                                                | 9.60 ms: 1.03x faster                                      |
| sqlglot_optimize         | 36.8 ms                                                | 35.9 ms: 1.02x faster                                      |
| tomli_loads              | 1.71 sec                                               | 1.67 sec: 1.02x faster                                     |
| float                    | 69.0 ms                                                | 68.2 ms: 1.01x faster                                      |
| bench_thread_pool        | 527 us                                                 | 523 us: 1.01x faster                                       |
| sqlglot_normalize        | 190 ms                                                 | 191 ms: 1.00x slower                                       |
| mdp                      | 1.63 sec                                               | 1.63 sec: 1.00x slower                                     |
| pidigits                 | 282 ms                                                 | 284 ms: 1.01x slower                                       |
| meteor_contest           | 77.7 ms                                                | 78.7 ms: 1.01x slower                                      |
| regex_v8                 | 17.1 ms                                                | 17.4 ms: 1.01x slower                                      |
| gc_traversal             | 2.36 ms                                                | 2.40 ms: 1.02x slower                                      |
| unpickle                 | 8.80 us                                                | 8.99 us: 1.02x slower                                      |
| pathlib                  | 24.5 ms                                                | 25.3 ms: 1.03x slower                                      |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                      |
| regex_effbot             | 2.46 ms                                                | 2.56 ms: 1.04x slower                                      |
| pickle                   | 6.97 us                                                | 7.36 us: 1.06x slower                                      |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.07x slower                                      |
| fannkuch                 | 303 ms                                                 | 324 ms: 1.07x slower                                       |
| pickle_list              | 2.74 us                                                | 2.93 us: 1.07x slower                                      |
| spectral_norm            | 94.8 ms                                                | 102 ms: 1.08x slower                                       |
| nqueens                  | 63.8 ms                                                | 69.7 ms: 1.09x slower                                      |
| scimark_fft              | 224 ms                                                 | 246 ms: 1.10x slower                                       |
| unpickle_list            | 2.69 us                                                | 2.98 us: 1.11x slower                                      |
| xml_etree_generate       | 53.5 ms                                                | 59.6 ms: 1.11x slower                                      |
| xml_etree_iterparse      | 72.1 ms                                                | 81.1 ms: 1.12x slower                                      |
| sqlite_synth             | 1.46 us                                                | 1.64 us: 1.13x slower                                      |
| coverage                 | 41.5 ms                                                | 47.9 ms: 1.16x slower                                      |
| python_startup           | 10.9 ms                                                | 12.7 ms: 1.16x slower                                      |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 4.04 ms: 1.18x slower                                      |
| bench_mp_pool            | 37.4 ms                                                | 44.8 ms: 1.20x slower                                      |
| async_generators         | 231 ms                                                 | 301 ms: 1.30x slower                                       |
| telco                    | 3.49 ms                                                | 4.63 ms: 1.33x slower                                      |
| python_startup_no_site   | 7.91 ms                                                | 11.4 ms: 1.44x slower                                      |
| Geometric mean           | (ref)                                                  | 1.12x faster                                               |

Benchmark hidden because not significant (3): xml_etree_parse, asyncio_websockets, hexiom
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.04x


# Memory

- memory change: 1.11x