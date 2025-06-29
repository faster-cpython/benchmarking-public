# Results vs. 3.12.0

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.230x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.15x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 288 ms: 1.32x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.11 sec: 1.27x slower                                                     |
| Geometric mean | (ref)                                                       | 1.29x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 551 ms: 1.40x faster                                                       |
| async_tree_io              | 731 ms                                                      | 531 ms: 1.38x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 284 ms: 1.29x faster                                                       |
| async_tree_none            | 291 ms                                                      | 232 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 228 ms: 1.25x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 285 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 430 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 432 ms: 1.13x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.26x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 56.2 ms: 1.28x faster                                                      |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| float          | 56.8 ms                                                     | 78.7 ms: 1.39x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.74 ms: 1.08x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.6 ms: 1.16x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 120 ms: 1.37x slower                                                       |
| Geometric mean | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_list        | 2.75 us                                                     | 3.08 us: 1.12x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 105 ms: 1.13x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.56 sec: 1.14x slower                                                     |
| unpickle_pure_python | 133 us                                                      | 157 us: 1.18x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 22.6 us: 1.23x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 71.8 ms: 1.29x slower                                                      |
| pickle               | 7.43 us                                                     | 9.86 us: 1.33x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 87.8 ms: 1.35x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 52.1 ms: 1.38x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.93 us: 1.39x slower                                                      |
| unpickle             | 8.18 us                                                     | 11.6 us: 1.42x slower                                                      |
| json_loads           | 13.9 us                                                     | 20.9 us: 1.50x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 8.63 ms: 1.52x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 329 us: 1.68x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.32x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.9 ms: 1.23x slower                                                      |
| python_startup         | 19.5 ms                                                     | 27.2 ms: 1.40x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.25 ms: 1.02x slower                                                      |
| django_template | 22.9 ms                                                     | 38.0 ms: 1.66x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.30x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 34.8 ms: 2.31x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 551 ms: 1.40x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.51 sec: 1.39x faster                                                     |
| async_tree_io              | 731 ms                                                      | 531 ms: 1.38x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 284 ms: 1.29x faster                                                       |
| nbody                      | 71.9 ms                                                     | 56.2 ms: 1.28x faster                                                      |
| async_tree_none            | 291 ms                                                      | 232 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 228 ms: 1.25x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 285 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 430 ms: 1.17x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 432 ms: 1.13x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.73 us: 1.01x faster                                                      |
| mako                       | 7.09 ms                                                     | 7.25 ms: 1.02x slower                                                      |
| scimark_fft                | 184 ms                                                      | 189 ms: 1.02x slower                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.74 ms: 1.08x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.80 ms: 1.09x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 81.6 ms: 1.09x slower                                                      |
| comprehensions             | 14.1 us                                                     | 15.8 us: 1.12x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.08 us: 1.12x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 105 ms: 1.13x slower                                                       |
| deepcopy                   | 238 us                                                      | 271 us: 1.14x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.56 sec: 1.14x slower                                                     |
| fannkuch                   | 247 ms                                                      | 284 ms: 1.15x slower                                                       |
| bench_thread_pool          | 857 us                                                      | 988 us: 1.15x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 16.6 ms: 1.16x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 569 ms: 1.17x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 157 us: 1.18x slower                                                       |
| dulwich_log                | 44.3 ms                                                     | 52.2 ms: 1.18x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.9 ms: 1.23x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 22.6 us: 1.23x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 115 ms: 1.25x slower                                                       |
| docutils                   | 1.66 sec                                                    | 2.11 sec: 1.27x slower                                                     |
| telco                      | 4.13 ms                                                     | 5.24 ms: 1.27x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 62.0 ms: 1.28x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 71.8 ms: 1.29x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 670 ms: 1.31x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.37 sec: 1.31x slower                                                     |
| sympy_integrate            | 13.0 ms                                                     | 17.0 ms: 1.31x slower                                                      |
| json                       | 3.05 ms                                                     | 3.99 ms: 1.31x slower                                                      |
| pyflate                    | 295 ms                                                      | 387 ms: 1.31x slower                                                       |
| 2to3                       | 218 ms                                                      | 288 ms: 1.32x slower                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.77 us: 1.33x slower                                                      |
| pickle                     | 7.43 us                                                     | 9.86 us: 1.33x slower                                                      |
| pycparser                  | 699 ms                                                      | 927 ms: 1.33x slower                                                       |
| sympy_str                  | 175 ms                                                      | 233 ms: 1.33x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 87.8 ms: 1.35x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 120 ms: 1.37x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 52.1 ms: 1.38x slower                                                      |
| float                      | 56.8 ms                                                     | 78.7 ms: 1.39x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.93 us: 1.39x slower                                                      |
| python_startup             | 19.5 ms                                                     | 27.2 ms: 1.40x slower                                                      |
| unpickle                   | 8.18 us                                                     | 11.6 us: 1.42x slower                                                      |
| sympy_expand               | 284 ms                                                      | 404 ms: 1.42x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 90.4 ms: 1.44x slower                                                      |
| deepcopy_memo              | 23.7 us                                                     | 35.1 us: 1.48x slower                                                      |
| async_generators           | 239 ms                                                      | 355 ms: 1.48x slower                                                       |
| logging_format             | 6.72 us                                                     | 10.1 us: 1.50x slower                                                      |
| go                         | 91.6 ms                                                     | 137 ms: 1.50x slower                                                       |
| json_loads                 | 13.9 us                                                     | 20.9 us: 1.50x slower                                                      |
| logging_simple             | 6.28 us                                                     | 9.44 us: 1.50x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 8.63 ms: 1.52x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 105 ms: 1.52x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 144 us: 1.52x slower                                                       |
| chaos                      | 43.3 ms                                                     | 66.0 ms: 1.52x slower                                                      |
| raytrace                   | 192 ms                                                      | 307 ms: 1.59x slower                                                       |
| generators                 | 22.5 ms                                                     | 37.3 ms: 1.65x slower                                                      |
| django_template            | 22.9 ms                                                     | 38.0 ms: 1.66x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 329 us: 1.68x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 73.7 ms: 1.69x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 135 ms: 1.71x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 115 ms: 1.72x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 25.7 ms: 1.80x slower                                                      |
| richards                   | 28.4 ms                                                     | 51.7 ms: 1.82x slower                                                      |
| richards_super             | 32.1 ms                                                     | 58.5 ms: 1.82x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.85 ms: 1.87x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 7.80 ms: 1.90x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.48 ms: 1.97x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 122 ms: 2.07x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 77.6 ns: 2.07x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 4.57 ms: 2.12x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 501 ns: 8.29x slower                                                       |
| coverage                   | 40.8 ms                                                     | 473 ms: 11.59x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.32x slower                                                               |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250614-3.15.0a0-2e15a50-JIT/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.230x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.21x
- 95% likely to have a slowdown of 1.17x
- 99% likely to have a slowdown of 1.15x

# Memory
- memory change: unknown