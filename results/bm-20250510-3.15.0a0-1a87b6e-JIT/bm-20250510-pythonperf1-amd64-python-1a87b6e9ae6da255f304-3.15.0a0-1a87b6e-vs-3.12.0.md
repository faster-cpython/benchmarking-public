# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-amd64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.073x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                     |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 399 ms: 1.93x faster                                                       |
| async_tree_io              | 731 ms                                                      | 398 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                       |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 335 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.4 ms: 1.28x faster                                                      |
| nbody          | 71.9 ms                                                     | 58.0 ms: 1.24x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.6 ms: 1.10x faster                                                      |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 13.9 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                     |
| unpickle_pure_python | 133 us                                                      | 118 us: 1.13x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 51.4 ms: 1.09x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 90.8 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.3 ms: 1.01x faster                                                      |
| unpickle             | 8.18 us                                                     | 8.48 us: 1.04x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.87 us: 1.04x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.07x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 209 us: 1.07x slower                                                       |
| pickle               | 7.43 us                                                     | 8.29 us: 1.11x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.6 us: 1.12x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.75 ms: 1.18x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.47 us: 1.23x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.0 ms: 1.23x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.7 ms: 1.37x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.66 ms: 1.25x faster                                                      |
| django_template | 22.9 ms                                                     | 24.5 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.6 ms: 2.47x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 399 ms: 1.93x faster                                                       |
| async_tree_io              | 731 ms                                                      | 398 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                       |
| mdp                        | 1.37 sec                                                    | 802 ms: 1.71x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                       |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 335 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.47 sec: 1.42x faster                                                     |
| deepcopy                   | 238 us                                                      | 176 us: 1.36x faster                                                       |
| float                      | 56.8 ms                                                     | 44.4 ms: 1.28x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.66 ms: 1.25x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 19.0 us: 1.25x faster                                                      |
| nbody                      | 71.9 ms                                                     | 58.0 ms: 1.24x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.5 us: 1.23x faster                                                      |
| scimark_fft                | 184 ms                                                      | 156 ms: 1.18x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                     |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                      |
| go                         | 91.6 ms                                                     | 79.6 ms: 1.15x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 118 us: 1.13x faster                                                       |
| chaos                      | 43.3 ms                                                     | 38.7 ms: 1.12x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.30 ms: 1.11x faster                                                      |
| raytrace                   | 192 ms                                                      | 175 ms: 1.10x faster                                                       |
| pyflate                    | 295 ms                                                      | 268 ms: 1.10x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 79.6 ms: 1.10x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 60.9 ms: 1.10x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 51.4 ms: 1.09x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.9 ms: 1.07x faster                                                      |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 481 ms: 1.07x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 991 ms: 1.06x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 74.9 ms: 1.05x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.3 ms: 1.05x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 60.1 ms: 1.04x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.8 ms: 1.04x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.04x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.9 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.6 ms: 1.03x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.6 ms: 1.03x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 90.8 ms: 1.03x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.9 ms: 1.02x faster                                                      |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.02x faster                                                       |
| json                       | 3.05 ms                                                     | 2.99 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| richards_super             | 32.1 ms                                                     | 31.6 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.3 ms: 1.01x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 59.5 ms: 1.01x slower                                                      |
| fannkuch                   | 247 ms                                                      | 249 ms: 1.01x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                     |
| meteor_contest             | 74.6 ms                                                     | 75.8 ms: 1.02x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 876 us: 1.02x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.20 ms: 1.02x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.50 us: 1.04x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.48 us: 1.04x slower                                                      |
| logging_format             | 6.72 us                                                     | 7.00 us: 1.04x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.87 us: 1.04x slower                                                      |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                       |
| sympy_expand               | 284 ms                                                      | 297 ms: 1.05x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.40 ms: 1.07x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.5 ms: 1.07x slower                                                      |
| async_generators           | 239 ms                                                      | 256 ms: 1.07x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.07x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                                       |
| pickle                     | 7.43 us                                                     | 8.29 us: 1.11x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 41.8 ns: 1.12x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 20.6 us: 1.12x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 548 ms: 1.12x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 108 us: 1.14x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.75 ms: 1.18x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.47 us: 1.23x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 20.0 ms: 1.23x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.7 ms: 1.37x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 97.1 ms: 1.40x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.19 ms: 1.44x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.34 ms: 1.78x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 328 ns: 5.43x slower                                                       |
| coverage                   | 40.8 ms                                                     | 300 ms: 7.35x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (2): deltablue, pycparser
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.073x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown