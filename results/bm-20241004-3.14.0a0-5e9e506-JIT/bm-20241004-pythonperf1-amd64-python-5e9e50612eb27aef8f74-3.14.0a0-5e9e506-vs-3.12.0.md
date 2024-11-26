# Results vs. 3.12.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: windows-amd64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.016x faster
- HPT reliability: 55.25%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 253 ms: 1.16x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.95 sec: 1.17x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 98.2 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 202 ms: 1.41x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 262 ms: 1.40x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 574 ms: 1.34x faster                                                       |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                       |
| async_tree_io              | 731 ms                                                      | 565 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 384 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 401 ms: 1.25x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 282 ms: 1.20x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 49.4 ms: 1.46x faster                                                      |
| float          | 56.8 ms                                                     | 47.2 ms: 1.20x faster                                                      |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 95.7 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 50.5 ms: 1.11x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.30 sec: 1.05x faster                                                     |
| pickle_list          | 2.83 us                                                     | 2.72 us: 1.04x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 17.8 us: 1.04x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                                      |
| pickle               | 7.43 us                                                     | 7.24 us: 1.03x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 198 us: 1.01x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 5.84 ms: 1.03x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 95.8 ms: 1.03x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.83 us: 1.03x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.94 us: 1.09x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 147 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.5 ms: 1.14x slower                                                      |
| python_startup         | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 4.99 ms: 1.42x faster                                                      |
| django_template | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 16.2 us: 1.46x faster                                                      |
| nbody                      | 71.9 ms                                                     | 49.4 ms: 1.46x faster                                                      |
| mako                       | 7.09 ms                                                     | 4.99 ms: 1.42x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 202 ms: 1.41x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 262 ms: 1.40x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.54 sec: 1.36x faster                                                     |
| async_tree_io_tg           | 771 ms                                                      | 574 ms: 1.34x faster                                                       |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                       |
| async_tree_io              | 731 ms                                                      | 565 ms: 1.29x faster                                                       |
| deepcopy                   | 238 us                                                      | 186 us: 1.28x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 384 ms: 1.27x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 52.6 ms: 1.27x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 61.9 ms: 1.27x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 401 ms: 1.25x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.6 us: 1.22x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.11 ms: 1.21x faster                                                      |
| scimark_fft                | 184 ms                                                      | 153 ms: 1.21x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 282 ms: 1.20x faster                                                       |
| float                      | 56.8 ms                                                     | 47.2 ms: 1.20x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 40.6 ms: 1.20x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 36.6 ms: 1.19x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.16x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 450 ms: 1.14x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 923 ms: 1.13x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 50.5 ms: 1.11x faster                                                      |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 55.7 ms: 1.06x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.30 sec: 1.05x faster                                                     |
| chaos                      | 43.3 ms                                                     | 41.5 ms: 1.04x faster                                                      |
| pickle_list                | 2.83 us                                                     | 2.72 us: 1.04x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 58.2 ns: 1.04x faster                                                      |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 17.8 us: 1.04x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.24 us: 1.03x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 43.2 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.15 us: 1.02x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.63 us: 1.01x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 75.4 ms: 1.01x slower                                                      |
| pathlib                    | 80.5 ms                                                     | 81.3 ms: 1.01x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 198 us: 1.01x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.84 ms: 1.03x slower                                                      |
| fannkuch                   | 247 ms                                                      | 254 ms: 1.03x slower                                                       |
| generators                 | 22.5 ms                                                     | 23.2 ms: 1.03x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 95.8 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.83 us: 1.03x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 65.1 ms: 1.04x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| pyflate                    | 295 ms                                                      | 310 ms: 1.05x slower                                                       |
| raytrace                   | 192 ms                                                      | 202 ms: 1.05x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.46 ms: 1.08x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.34 ms: 1.08x slower                                                      |
| async_generators           | 239 ms                                                      | 260 ms: 1.09x slower                                                       |
| pycparser                  | 699 ms                                                      | 759 ms: 1.09x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.94 us: 1.09x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 95.7 ms: 1.09x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 205 ms: 1.09x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 98.2 ms: 1.10x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 887 us: 1.10x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 147 us: 1.11x slower                                                       |
| sympy_str                  | 175 ms                                                      | 196 ms: 1.12x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 104 ms: 1.14x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.5 ms: 1.14x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.17 ms: 1.15x slower                                                      |
| 2to3                       | 218 ms                                                      | 253 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.95 sec: 1.17x slower                                                     |
| mdp                        | 1.37 sec                                                    | 1.61 sec: 1.17x slower                                                     |
| sympy_expand               | 284 ms                                                      | 334 ms: 1.18x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 15.6 ms: 1.20x slower                                                      |
| richards_super             | 32.1 ms                                                     | 38.6 ms: 1.20x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.6 ms: 1.21x slower                                                      |
| richards                   | 28.4 ms                                                     | 34.5 ms: 1.22x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 42.9 ms: 1.24x slower                                                      |
| python_startup             | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.93 ms: 1.27x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 88.9 ms: 1.29x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 5.28 ms: 1.29x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 673 ms: 1.38x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 58.5 ns: 1.56x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.38 ms: 1.84x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (3): bench_thread_pool, go, json
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.016x faster
# HPT report

- Reliability score: 55.25% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown