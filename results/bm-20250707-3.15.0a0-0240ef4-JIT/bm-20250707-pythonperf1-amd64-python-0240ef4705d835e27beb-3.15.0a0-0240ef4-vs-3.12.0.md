# Results vs. 3.12.0

- fork: python
- ref: 0240ef4705d835e27beb
- machine: windows-amd64
- commit hash: 0240ef4
- commit date: 2025-07-07
- overall geometric mean: 1.126x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 384 ms: 2.01x faster                                                       |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 206 ms: 1.78x faster                                                       |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.74x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.71x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.47x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 333 ms: 1.47x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 55.0 ms: 1.31x faster                                                      |
| float          | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                      |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.3 ms: 1.12x faster                                                      |
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.5 ms: 1.06x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 108 us: 1.24x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.13 sec: 1.21x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 49.8 ms: 1.12x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.0 ms: 1.08x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 87.8 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 202 us: 1.04x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.23 ms: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.40 ms: 1.31x faster                                                      |
| django_template | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.6 ms: 2.54x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 384 ms: 2.01x faster                                                       |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 206 ms: 1.78x faster                                                       |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.74x faster                                                       |
| mdp                        | 1.37 sec                                                    | 799 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.71x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.47x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 333 ms: 1.47x faster                                                       |
| deepcopy                   | 238 us                                                      | 170 us: 1.40x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.35x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 17.9 us: 1.33x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.40 ms: 1.31x faster                                                      |
| nbody                      | 71.9 ms                                                     | 55.0 ms: 1.31x faster                                                      |
| float                      | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 108 us: 1.24x faster                                                       |
| scimark_fft                | 184 ms                                                      | 153 ms: 1.21x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.13 sec: 1.21x faster                                                     |
| go                         | 91.6 ms                                                     | 76.2 ms: 1.20x faster                                                      |
| pyflate                    | 295 ms                                                      | 253 ms: 1.17x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.83 us: 1.14x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.13x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.27 ms: 1.13x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 931 ms: 1.12x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 49.8 ms: 1.12x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.3 ms: 1.12x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 460 ms: 1.12x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 54.4 ns: 1.11x faster                                                      |
| fannkuch                   | 247 ms                                                      | 222 ms: 1.11x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.9 ms: 1.10x faster                                                      |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                       |
| raytrace                   | 192 ms                                                      | 177 ms: 1.09x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.9 ms: 1.08x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.3 ms: 1.08x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.0 ms: 1.08x faster                                                      |
| richards_super             | 32.1 ms                                                     | 29.9 ms: 1.07x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.4 ms: 1.07x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 70.4 ms: 1.06x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 87.8 ms: 1.06x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 59.3 ms: 1.06x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.5 ms: 1.06x faster                                                      |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 87.4 ms: 1.05x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.4 ms: 1.04x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.02 us: 1.04x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.51 us: 1.03x faster                                                      |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.6 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                      |
| json                       | 3.05 ms                                                     | 2.98 ms: 1.02x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 77.2 ms: 1.02x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| pycparser                  | 699 ms                                                      | 691 ms: 1.01x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.15 ms: 1.01x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.01x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 68.2 ms: 1.02x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 60.1 ms: 1.02x slower                                                      |
| async_generators           | 239 ms                                                      | 247 ms: 1.03x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 202 us: 1.04x slower                                                       |
| sympy_expand               | 284 ms                                                      | 294 ms: 1.04x slower                                                       |
| django_template            | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.34 ms: 1.05x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.23 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| coverage                   | 40.8 ms                                                     | 51.0 ms: 1.25x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.11 ms: 1.39x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.75x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): 2to3
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250707-3.15.0a0-0240ef4-JIT/bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.126x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown