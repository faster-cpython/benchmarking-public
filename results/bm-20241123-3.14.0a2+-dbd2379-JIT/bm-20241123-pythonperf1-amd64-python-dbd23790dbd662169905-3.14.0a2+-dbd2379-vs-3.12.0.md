# Results vs. 3.12.0

- fork: python
- ref: dbd23790dbd662169905
- machine: windows-amd64
- commit hash: dbd2379
- commit date: 2024-11-23
- overall geometric mean: 1.040x faster
- HPT reliability: 94.37%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.79 sec: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 257 ms: 1.43x faster                                                        |
| async_tree_none            | 291 ms                                                      | 209 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 207 ms: 1.38x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 579 ms: 1.33x faster                                                        |
| async_tree_io              | 731 ms                                                      | 588 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 411 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 401 ms: 1.22x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 279 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 52.4 ms: 1.37x faster                                                       |
| float          | 56.8 ms                                                     | 47.2 ms: 1.20x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.49 ms: 1.09x faster                                                       |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 85.1 ms: 1.03x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 15.1 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 108 us: 1.24x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 50.7 ms: 1.10x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.26 sec: 1.09x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.8 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.03x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 211 us: 1.08x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.1 ms: 1.06x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.2 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.15 ms: 1.38x faster                                                       |
| django_template | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 15.8 us: 1.51x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 257 ms: 1.43x faster                                                        |
| async_tree_none            | 291 ms                                                      | 209 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 207 ms: 1.38x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.15 ms: 1.38x faster                                                       |
| nbody                      | 71.9 ms                                                     | 52.4 ms: 1.37x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 579 ms: 1.33x faster                                                        |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 53.3 ms: 1.26x faster                                                       |
| async_tree_io              | 731 ms                                                      | 588 ms: 1.24x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 108 us: 1.24x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 64.1 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 411 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 401 ms: 1.22x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 279 ms: 1.22x faster                                                        |
| scimark_fft                | 184 ms                                                      | 153 ms: 1.21x faster                                                        |
| float                      | 56.8 ms                                                     | 47.2 ms: 1.20x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 36.4 ms: 1.20x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 40.4 ms: 1.20x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.20x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.24 ms: 1.14x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.88 us: 1.11x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 50.7 ms: 1.10x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.7 ms: 1.09x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.49 ms: 1.09x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.26 sec: 1.09x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 473 ms: 1.08x faster                                                        |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 970 ms: 1.08x faster                                                        |
| chaos                      | 43.3 ms                                                     | 40.5 ms: 1.07x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 55.2 ms: 1.07x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 806 us: 1.06x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.66 us: 1.06x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 35.8 ms: 1.05x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 76.5 ms: 1.05x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 57.5 ns: 1.05x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                       |
| pyflate                    | 295 ms                                                      | 284 ms: 1.04x faster                                                        |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| meteor_contest             | 74.6 ms                                                     | 72.4 ms: 1.03x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.10 us: 1.03x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.53 us: 1.03x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 85.1 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                       |
| json                       | 3.05 ms                                                     | 2.97 ms: 1.02x faster                                                       |
| generators                 | 22.5 ms                                                     | 22.2 ms: 1.02x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 63.4 ms: 1.01x slower                                                       |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                        |
| sympy_sum                  | 91.5 ms                                                     | 93.7 ms: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                       |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| fannkuch                   | 247 ms                                                      | 258 ms: 1.04x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.33 ms: 1.05x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.1 ms: 1.06x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.1 ms: 1.06x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.9 ms: 1.08x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.79 sec: 1.08x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 211 us: 1.08x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.34 ms: 1.08x slower                                                       |
| sympy_expand               | 284 ms                                                      | 307 ms: 1.08x slower                                                        |
| raytrace                   | 192 ms                                                      | 209 ms: 1.09x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 878 us: 1.09x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 205 ms: 1.09x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.10x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 37.9 ms: 1.10x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                       |
| async_generators           | 239 ms                                                      | 264 ms: 1.10x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.13 ms: 1.11x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.0 ms: 1.15x slower                                                       |
| richards_super             | 32.1 ms                                                     | 37.3 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.17x slower                                                        |
| richards                   | 28.4 ms                                                     | 33.3 ms: 1.17x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 82.2 ms: 1.19x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.2 ms: 1.19x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.85 ms: 1.21x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.99 ms: 1.22x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.31 ms: 1.75x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (3): go, xml_etree_parse, pycparser
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241123-3.14.0a2+-dbd2379-JIT/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.040x faster
# HPT report

- Reliability score: 94.37% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown