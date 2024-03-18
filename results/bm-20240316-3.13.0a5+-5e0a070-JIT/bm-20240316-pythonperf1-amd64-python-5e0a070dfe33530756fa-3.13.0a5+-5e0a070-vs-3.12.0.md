# Results vs. 3.12.0

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-amd64
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                        |
| chameleon      | 4.98 ms                                                     | 4.74 ms: 1.05x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.60 sec: 1.04x faster                                                      |
| tornado_http   | 89.5 ms                                                     | 85.1 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 291 ms                                                      | 262 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 446 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 342 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 471 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 725 ms: 1.06x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 269 ms: 1.06x faster                                                        |
| async_tree_io              | 731 ms                                                      | 710 ms: 1.03x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 58.2 ms: 1.24x faster                                                       |
| float          | 56.8 ms                                                     | 48.8 ms: 1.16x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 83.6 ms: 1.05x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.6 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 178 us: 1.10x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 52.7 ms: 1.06x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 17.4 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.8 ms: 1.05x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                       |
| pickle               | 7.43 us                                                     | 7.15 us: 1.04x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 128 us: 1.04x faster                                                        |
| json_dumps           | 5.70 ms                                                     | 5.53 ms: 1.03x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 91.0 ms: 1.02x faster                                                       |
| json_loads           | 13.9 us                                                     | 13.6 us: 1.02x faster                                                       |
| pickle_list          | 2.83 us                                                     | 2.93 us: 1.04x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.56 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 24.0 ms: 1.23x slower                                                       |
| python_startup_no_site | 16.2 ms                                                     | 21.8 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.65 ms: 1.25x faster                                                       |
| django_template | 22.9 ms                                                     | 21.4 ms: 1.07x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols   | 95.1 us                                                     | 68.7 us: 1.38x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.38x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 51.8 ms: 1.29x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.65 ms: 1.25x faster                                                       |
| nbody                      | 71.9 ms                                                     | 58.2 ms: 1.24x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.71 sec: 1.23x faster                                                      |
| mypy2                      | 509 ms                                                      | 436 ms: 1.17x faster                                                        |
| float                      | 56.8 ms                                                     | 48.8 ms: 1.16x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.24 ms: 1.14x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.14x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                       |
| async_tree_none            | 291 ms                                                      | 262 ms: 1.11x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 43.7 ms: 1.11x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 55.1 ns: 1.10x faster                                                       |
| fannkuch                   | 247 ms                                                      | 225 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 446 ms: 1.10x faster                                                        |
| pickle_pure_python         | 195 us                                                      | 178 us: 1.10x faster                                                        |
| chaos                      | 43.3 ms                                                     | 39.7 ms: 1.09x faster                                                       |
| scimark_fft                | 184 ms                                                      | 169 ms: 1.09x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 963 ms: 1.09x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 473 ms: 1.08x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 21.9 us: 1.08x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.25 us: 1.08x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 342 ms: 1.07x faster                                                        |
| raytrace                   | 192 ms                                                      | 179 ms: 1.07x faster                                                        |
| sympy_str                  | 175 ms                                                      | 163 ms: 1.07x faster                                                        |
| logging_simple             | 6.28 us                                                     | 5.86 us: 1.07x faster                                                       |
| django_template            | 22.9 ms                                                     | 21.4 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.96 us: 1.07x faster                                                       |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 471 ms: 1.07x faster                                                        |
| sqlglot_normalize          | 187 ms                                                      | 175 ms: 1.07x faster                                                        |
| deepcopy                   | 238 us                                                      | 224 us: 1.06x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 725 ms: 1.06x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 269 ms: 1.06x faster                                                        |
| deltablue                  | 2.16 ms                                                     | 2.03 ms: 1.06x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 52.7 ms: 1.06x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.8 ms: 1.06x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 17.4 us: 1.06x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.8 ms: 1.05x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 59.7 ms: 1.05x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 85.1 ms: 1.05x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.6 ms: 1.05x faster                                                       |
| chameleon                  | 4.98 ms                                                     | 4.74 ms: 1.05x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 76.8 ms: 1.05x faster                                                       |
| pyflate                    | 295 ms                                                      | 281 ms: 1.05x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 83.6 ms: 1.05x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 87.6 ms: 1.04x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.15 us: 1.04x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 128 us: 1.04x faster                                                        |
| docutils                   | 1.66 sec                                                    | 1.60 sec: 1.04x faster                                                      |
| richards_super             | 32.1 ms                                                     | 31.1 ms: 1.03x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 830 us: 1.03x faster                                                        |
| async_tree_io              | 731 ms                                                      | 710 ms: 1.03x faster                                                        |
| sqlglot_parse              | 804 us                                                      | 781 us: 1.03x faster                                                        |
| json_dumps                 | 5.70 ms                                                     | 5.53 ms: 1.03x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 474 ms: 1.03x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 91.0 ms: 1.02x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1000 us: 1.02x faster                                                       |
| json_loads                 | 13.9 us                                                     | 13.6 us: 1.02x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.9 ms: 1.02x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 73.4 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| sympy_expand               | 284 ms                                                      | 279 ms: 1.02x faster                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.51 ms: 1.01x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.1 ms: 1.01x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 70.2 ms: 1.01x slower                                                       |
| aiohttp                    | 884 us                                                      | 899 us: 1.02x slower                                                        |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 14.6 ms: 1.02x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| pickle_list                | 2.83 us                                                     | 2.93 us: 1.04x slower                                                       |
| go                         | 91.6 ms                                                     | 95.2 ms: 1.04x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.28 ms: 1.04x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.56 us: 1.05x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 83.5 ms: 1.06x slower                                                       |
| json                       | 3.05 ms                                                     | 3.27 ms: 1.07x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.60 ms: 1.11x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.5 ms: 1.14x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 71.9 ms: 1.22x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.0 ms: 1.23x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 46.9 ns: 1.25x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 21.8 ms: 1.34x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (6): pycparser, create_gc_cycles, async_tree_memoization, sqlglot_optimize, async_generators, unpickle_list
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240316-3.13.0a5+-5e0a070-JIT/bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x


# Memory

- memory change: unknown