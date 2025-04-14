# Results vs. 3.12.0

- fork: faster-cpython
- ref: close_escapes_2
- machine: windows-amd64
- commit hash: 620dde2
- commit date: 2025-01-29
- overall geometric mean: 1.006x slower
- HPT reliability: 98.54%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 233 ms: 1.07x slower                                                             |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                           |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 419 ms: 1.84x faster                                                             |
| async_tree_io              | 731 ms                                                      | 431 ms: 1.69x faster                                                             |
| async_tree_memoization_tg  | 367 ms                                                      | 220 ms: 1.67x faster                                                             |
| async_tree_none_tg         | 285 ms                                                      | 180 ms: 1.58x faster                                                             |
| async_tree_none            | 291 ms                                                      | 193 ms: 1.51x faster                                                             |
| async_tree_memoization     | 339 ms                                                      | 228 ms: 1.49x faster                                                             |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                             |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 349 ms: 1.40x faster                                                             |
| Geometric mean             | (ref)                                                       | 1.57x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 52.6 ms: 1.08x faster                                                            |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                             |
| nbody          | 71.9 ms                                                     | 77.1 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.43 ms: 1.13x faster                                                            |
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                             |
| regex_compile  | 87.5 ms                                                     | 89.5 ms: 1.02x slower                                                            |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 87.5 ms: 1.06x faster                                                            |
| xml_etree_generate   | 55.8 ms                                                     | 58.6 ms: 1.05x slower                                                            |
| tomli_loads          | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                           |
| xml_etree_process    | 37.7 ms                                                     | 41.3 ms: 1.09x slower                                                            |
| json_loads           | 13.9 us                                                     | 15.4 us: 1.11x slower                                                            |
| json_dumps           | 5.70 ms                                                     | 6.81 ms: 1.20x slower                                                            |
| pickle_pure_python   | 195 us                                                      | 238 us: 1.22x slower                                                             |
| unpickle_pure_python | 133 us                                                      | 164 us: 1.23x slower                                                             |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                            |
| python_startup         | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                            |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.88 ms: 1.03x faster                                                            |
| django_template | 22.9 ms                                                     | 25.6 ms: 1.12x slower                                                            |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 419 ms: 1.84x faster                                                             |
| async_tree_io              | 731 ms                                                      | 431 ms: 1.69x faster                                                             |
| async_tree_memoization_tg  | 367 ms                                                      | 220 ms: 1.67x faster                                                             |
| async_tree_none_tg         | 285 ms                                                      | 180 ms: 1.58x faster                                                             |
| async_tree_none            | 291 ms                                                      | 193 ms: 1.51x faster                                                             |
| async_tree_memoization     | 339 ms                                                      | 228 ms: 1.49x faster                                                             |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                             |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 349 ms: 1.40x faster                                                             |
| deepcopy                   | 238 us                                                      | 187 us: 1.27x faster                                                             |
| regex_effbot               | 1.62 ms                                                     | 1.43 ms: 1.13x faster                                                            |
| deepcopy_memo              | 23.7 us                                                     | 21.4 us: 1.11x faster                                                            |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                             |
| deepcopy_reduce            | 2.09 us                                                     | 1.90 us: 1.10x faster                                                            |
| comprehensions             | 14.1 us                                                     | 12.9 us: 1.09x faster                                                            |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                            |
| float                      | 56.8 ms                                                     | 52.6 ms: 1.08x faster                                                            |
| xml_etree_parse            | 93.0 ms                                                     | 87.5 ms: 1.06x faster                                                            |
| async_generators           | 239 ms                                                      | 225 ms: 1.06x faster                                                             |
| generators                 | 22.5 ms                                                     | 21.6 ms: 1.04x faster                                                            |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                             |
| pathlib                    | 80.5 ms                                                     | 77.8 ms: 1.03x faster                                                            |
| mako                       | 7.09 ms                                                     | 6.88 ms: 1.03x faster                                                            |
| dulwich_log                | 44.3 ms                                                     | 43.3 ms: 1.02x faster                                                            |
| spectral_norm              | 66.9 ms                                                     | 66.3 ms: 1.01x faster                                                            |
| sympy_sum                  | 91.5 ms                                                     | 90.6 ms: 1.01x faster                                                            |
| go                         | 91.6 ms                                                     | 92.0 ms: 1.01x slower                                                            |
| logging_format             | 6.72 us                                                     | 6.76 us: 1.01x slower                                                            |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                           |
| crypto_pyaes               | 48.5 ms                                                     | 49.5 ms: 1.02x slower                                                            |
| meteor_contest             | 74.6 ms                                                     | 76.2 ms: 1.02x slower                                                            |
| regex_compile              | 87.5 ms                                                     | 89.5 ms: 1.02x slower                                                            |
| sympy_str                  | 175 ms                                                      | 180 ms: 1.03x slower                                                             |
| json                       | 3.05 ms                                                     | 3.18 ms: 1.04x slower                                                            |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.68 ms: 1.05x slower                                                            |
| coroutines                 | 14.3 ms                                                     | 15.0 ms: 1.05x slower                                                            |
| xml_etree_generate         | 55.8 ms                                                     | 58.6 ms: 1.05x slower                                                            |
| nqueens                    | 62.8 ms                                                     | 66.2 ms: 1.05x slower                                                            |
| tomli_loads                | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                           |
| sympy_integrate            | 13.0 ms                                                     | 13.7 ms: 1.06x slower                                                            |
| raytrace                   | 192 ms                                                      | 203 ms: 1.06x slower                                                             |
| sqlglot_optimize           | 34.5 ms                                                     | 36.6 ms: 1.06x slower                                                            |
| pyflate                    | 295 ms                                                      | 314 ms: 1.06x slower                                                             |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                           |
| 2to3                       | 218 ms                                                      | 233 ms: 1.07x slower                                                             |
| sqlglot_normalize          | 187 ms                                                      | 200 ms: 1.07x slower                                                             |
| nbody                      | 71.9 ms                                                     | 77.1 ms: 1.07x slower                                                            |
| pycparser                  | 699 ms                                                      | 750 ms: 1.07x slower                                                             |
| sympy_expand               | 284 ms                                                      | 306 ms: 1.08x slower                                                             |
| scimark_fft                | 184 ms                                                      | 199 ms: 1.08x slower                                                             |
| pprint_safe_repr           | 513 ms                                                      | 556 ms: 1.08x slower                                                             |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                            |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.09x slower                                                            |
| xml_etree_process          | 37.7 ms                                                     | 41.3 ms: 1.09x slower                                                            |
| deltablue                  | 2.16 ms                                                     | 2.38 ms: 1.10x slower                                                            |
| json_loads                 | 13.9 us                                                     | 15.4 us: 1.11x slower                                                            |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                            |
| django_template            | 22.9 ms                                                     | 25.6 ms: 1.12x slower                                                            |
| sqlglot_parse              | 804 us                                                      | 901 us: 1.12x slower                                                             |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.7 ms: 1.14x slower                                                            |
| logging_silent             | 60.5 ns                                                     | 69.1 ns: 1.14x slower                                                            |
| hexiom                     | 4.10 ms                                                     | 4.70 ms: 1.15x slower                                                            |
| richards_super             | 32.1 ms                                                     | 37.0 ms: 1.15x slower                                                            |
| richards                   | 28.4 ms                                                     | 32.8 ms: 1.15x slower                                                            |
| fannkuch                   | 247 ms                                                      | 286 ms: 1.16x slower                                                             |
| mdp                        | 1.37 sec                                                    | 1.62 sec: 1.18x slower                                                           |
| telco                      | 4.13 ms                                                     | 4.87 ms: 1.18x slower                                                            |
| scimark_lu                 | 58.9 ms                                                     | 70.1 ms: 1.19x slower                                                            |
| json_dumps                 | 5.70 ms                                                     | 6.81 ms: 1.20x slower                                                            |
| coverage                   | 40.8 ms                                                     | 49.2 ms: 1.20x slower                                                            |
| scimark_sor                | 78.8 ms                                                     | 95.4 ms: 1.21x slower                                                            |
| typing_runtime_protocols   | 95.1 us                                                     | 116 us: 1.22x slower                                                             |
| pickle_pure_python         | 195 us                                                      | 238 us: 1.22x slower                                                             |
| unpickle_pure_python       | 133 us                                                      | 164 us: 1.23x slower                                                             |
| python_startup             | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                            |
| bench_mp_pool              | 69.2 ms                                                     | 87.7 ms: 1.27x slower                                                            |
| gc_traversal               | 1.52 ms                                                     | 1.97 ms: 1.29x slower                                                            |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                            |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                     |

Benchmark hidden because not significant (4): xml_etree_iterparse, bench_thread_pool, chaos, logging_simple
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250129-3.14.0a4+-620dde2/bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.006x slower

# HPT report

- Reliability score: 98.54% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown