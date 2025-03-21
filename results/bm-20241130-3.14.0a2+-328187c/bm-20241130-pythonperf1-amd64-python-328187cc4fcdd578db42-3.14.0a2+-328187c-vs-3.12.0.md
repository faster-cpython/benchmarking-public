# Results vs. 3.12.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: windows-amd64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.025x slower
- HPT reliability: 99.84%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 253 ms: 1.45x faster                                                        |
| async_tree_none            | 291 ms                                                      | 212 ms: 1.37x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 208 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 582 ms: 1.32x faster                                                        |
| async_tree_io              | 731 ms                                                      | 581 ms: 1.26x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 406 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 419 ms: 1.20x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| nbody          | 71.9 ms                                                     | 79.3 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.44 ms: 1.12x faster                                                       |
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 91.5 ms: 1.05x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 94.8 ms: 1.02x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 58.2 ms: 1.04x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.9 us: 1.07x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.2 ms: 1.09x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 227 us: 1.16x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.17x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 7.08 ms: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.3 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.53 ms: 1.06x slower                                                       |
| django_template | 22.9 ms                                                     | 25.3 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 253 ms: 1.45x faster                                                        |
| async_tree_none            | 291 ms                                                      | 212 ms: 1.37x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 208 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 582 ms: 1.32x faster                                                        |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                        |
| async_tree_io              | 731 ms                                                      | 581 ms: 1.26x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 406 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 419 ms: 1.20x faster                                                        |
| comprehensions             | 14.1 us                                                     | 12.2 us: 1.16x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.44 ms: 1.12x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.3 us: 1.11x faster                                                       |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.09x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.93 us: 1.09x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 74.5 ms: 1.08x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 809 us: 1.06x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 43.0 ms: 1.03x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 89.7 ms: 1.02x faster                                                       |
| go                         | 91.6 ms                                                     | 89.7 ms: 1.02x faster                                                       |
| raytrace                   | 192 ms                                                      | 194 ms: 1.01x slower                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 49.1 ms: 1.01x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.38 us: 1.02x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 94.8 ms: 1.02x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                      |
| chaos                      | 43.3 ms                                                     | 44.3 ms: 1.02x slower                                                       |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                        |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| async_generators           | 239 ms                                                      | 248 ms: 1.04x slower                                                        |
| meteor_contest             | 74.6 ms                                                     | 77.5 ms: 1.04x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 65.3 ms: 1.04x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 58.2 ms: 1.04x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 91.5 ms: 1.05x slower                                                       |
| json                       | 3.05 ms                                                     | 3.21 ms: 1.05x slower                                                       |
| pycparser                  | 699 ms                                                      | 741 ms: 1.06x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 36.6 ms: 1.06x slower                                                       |
| mako                       | 7.09 ms                                                     | 7.53 ms: 1.06x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.31 ms: 1.07x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 200 ms: 1.07x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 63.4 ms: 1.08x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 556 ms: 1.08x slower                                                        |
| sympy_expand               | 284 ms                                                      | 308 ms: 1.08x slower                                                        |
| spectral_norm              | 66.9 ms                                                     | 72.7 ms: 1.09x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.09x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 41.2 ms: 1.09x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.80 ms: 1.09x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.3 ms: 1.10x slower                                                       |
| nbody                      | 71.9 ms                                                     | 79.3 ms: 1.10x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.13 ms: 1.11x slower                                                       |
| pyflate                    | 295 ms                                                      | 327 ms: 1.11x slower                                                        |
| logging_silent             | 60.5 ns                                                     | 67.4 ns: 1.11x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.8 ms: 1.12x slower                                                       |
| scimark_fft                | 184 ms                                                      | 206 ms: 1.12x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 4.58 ms: 1.12x slower                                                       |
| coverage                   | 40.8 ms                                                     | 45.6 ms: 1.12x slower                                                       |
| richards_super             | 32.1 ms                                                     | 36.5 ms: 1.14x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 919 us: 1.14x slower                                                        |
| richards                   | 28.4 ms                                                     | 32.8 ms: 1.15x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 227 us: 1.16x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 91.6 ms: 1.16x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.17x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 81.7 ms: 1.18x slower                                                       |
| fannkuch                   | 247 ms                                                      | 292 ms: 1.18x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.88 ms: 1.18x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.3 ms: 1.20x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.87 ms: 1.23x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 7.08 ms: 1.24x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.76x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (4): float, generators, logging_format, xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.025x slower

# HPT report

- Reliability score: 99.84% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown