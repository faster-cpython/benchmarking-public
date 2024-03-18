# Results vs. 3.12.0

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-amd64
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.01x slower
- HPT reliability: 84.64%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| chameleon      | 4.98 ms                                                     | 4.92 ms: 1.01x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                      |
| tornado_http   | 89.5 ms                                                     | 86.4 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 291 ms                                                      | 270 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 454 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 469 ms: 1.07x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 347 ms: 1.06x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 744 ms: 1.04x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 276 ms: 1.03x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 348 ms: 1.03x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| nbody          | 71.9 ms                                                     | 74.4 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                       |
| regex_compile  | 87.5 ms                                                     | 96.7 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 183 us: 1.07x faster                                                        |
| pickle               | 7.43 us                                                     | 7.19 us: 1.03x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 91.8 ms: 1.01x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 18.2 us: 1.01x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.72 us: 1.01x faster                                                       |
| json_loads           | 13.9 us                                                     | 13.8 us: 1.01x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.76 ms: 1.01x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 38.2 ms: 1.01x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.31 us: 1.02x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.24 us: 1.15x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 20.3 ms: 1.04x slower                                                       |
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.73 ms: 1.05x faster                                                       |
| django_template | 22.9 ms                                                     | 22.4 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.04x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols   | 95.1 us                                                     | 73.1 us: 1.30x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.71 sec: 1.22x faster                                                      |
| mypy2                      | 509 ms                                                      | 443 ms: 1.15x faster                                                        |
| comprehensions             | 14.1 us                                                     | 12.8 us: 1.10x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 54.9 ns: 1.10x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.7 ms: 1.09x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| async_tree_none            | 291 ms                                                      | 270 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 454 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 469 ms: 1.07x faster                                                        |
| pickle_pure_python         | 195 us                                                      | 183 us: 1.07x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.97 us: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.06x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 347 ms: 1.06x faster                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 65.7 ms: 1.05x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.73 ms: 1.05x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| tornado_http               | 89.5 ms                                                     | 86.4 ms: 1.04x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 744 ms: 1.04x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 77.8 ms: 1.03x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.19 us: 1.03x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 276 ms: 1.03x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 834 us: 1.03x faster                                                        |
| logging_format             | 6.72 us                                                     | 6.55 us: 1.03x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.12 us: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                       |
| django_template            | 22.9 ms                                                     | 22.4 ms: 1.02x faster                                                       |
| raytrace                   | 192 ms                                                      | 189 ms: 1.02x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 47.6 ms: 1.02x faster                                                       |
| deepcopy                   | 238 us                                                      | 234 us: 1.02x faster                                                        |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 91.8 ms: 1.01x faster                                                       |
| chameleon                  | 4.98 ms                                                     | 4.92 ms: 1.01x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.2 us: 1.01x faster                                                       |
| create_gc_cycles           | 752 us                                                      | 744 us: 1.01x faster                                                        |
| async_generators           | 239 ms                                                      | 237 ms: 1.01x faster                                                        |
| unpickle_list              | 2.75 us                                                     | 2.72 us: 1.01x faster                                                       |
| json_loads                 | 13.9 us                                                     | 13.8 us: 1.01x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 75.0 ms: 1.01x slower                                                       |
| chaos                      | 43.3 ms                                                     | 43.6 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 189 ms: 1.01x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 5.76 ms: 1.01x slower                                                       |
| richards                   | 28.4 ms                                                     | 28.7 ms: 1.01x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 38.2 ms: 1.01x slower                                                       |
| richards_super             | 32.1 ms                                                     | 32.5 ms: 1.01x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.01x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.31 us: 1.02x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 523 ms: 1.02x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 819 us: 1.02x slower                                                        |
| deepcopy_memo              | 23.7 us                                                     | 24.2 us: 1.02x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.04 ms: 1.02x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.02x slower                                                      |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| aiohttp                    | 884 us                                                      | 908 us: 1.03x slower                                                        |
| async_tree_memoization     | 339 ms                                                      | 348 ms: 1.03x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                       |
| nbody                      | 71.9 ms                                                     | 74.4 ms: 1.03x slower                                                       |
| pycparser                  | 699 ms                                                      | 725 ms: 1.04x slower                                                        |
| python_startup             | 19.5 ms                                                     | 20.3 ms: 1.04x slower                                                       |
| fannkuch                   | 247 ms                                                      | 260 ms: 1.06x slower                                                        |
| sympy_expand               | 284 ms                                                      | 301 ms: 1.06x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.9 ms: 1.07x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 68.1 ms: 1.09x slower                                                       |
| scimark_fft                | 184 ms                                                      | 201 ms: 1.09x slower                                                        |
| spectral_norm              | 66.9 ms                                                     | 73.0 ms: 1.09x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 40.9 ns: 1.09x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.51 sec: 1.10x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 96.7 ms: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                       |
| pyflate                    | 295 ms                                                      | 327 ms: 1.11x slower                                                        |
| coverage                   | 40.8 ms                                                     | 45.3 ms: 1.11x slower                                                       |
| go                         | 91.6 ms                                                     | 102 ms: 1.12x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.4 ms: 1.13x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 89.1 ms: 1.13x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.24 us: 1.15x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.76 ms: 1.15x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.17x slower                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.99 ms: 1.17x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.88 ms: 1.19x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 76.1 ms: 1.29x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (10): asyncio_tcp, async_tree_io, gc_traversal, xml_etree_generate, sympy_str, float, xml_etree_iterparse, dulwich_log, sympy_sum, json
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240316-3.13.0a5+-5e0a070-PYTHON_UOPS/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 84.64% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: unknown