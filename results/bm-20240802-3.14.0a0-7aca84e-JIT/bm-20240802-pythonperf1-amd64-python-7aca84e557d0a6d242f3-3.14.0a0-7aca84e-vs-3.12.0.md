# Results vs. 3.12.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-amd64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.05x faster
- HPT reliability: 94.76%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 242 ms: 1.11x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.85 sec: 1.12x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 95.2 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 194 ms: 1.47x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 251 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 540 ms: 1.43x faster                                                       |
| async_tree_none            | 291 ms                                                      | 214 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 379 ms: 1.32x faster                                                       |
| async_tree_io              | 731 ms                                                      | 553 ms: 1.32x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 395 ms: 1.24x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.36x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 50.1 ms: 1.43x faster                                                      |
| float          | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 91.0 ms: 1.04x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.26 sec: 1.08x faster                                                     |
| pickle_pure_python   | 195 us                                                      | 182 us: 1.07x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 52.6 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.8 ms: 1.06x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 95.5 ms: 1.03x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 138 us: 1.03x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 5.96 ms: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                      |
| python_startup_no_site | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.05 ms: 1.40x faster                                                      |
| django_template | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 15.7 us: 1.51x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 45.0 ms: 1.49x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 194 ms: 1.47x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 251 ms: 1.46x faster                                                       |
| nbody                      | 71.9 ms                                                     | 50.1 ms: 1.43x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 540 ms: 1.43x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.05 ms: 1.40x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.51 sec: 1.39x faster                                                     |
| async_tree_none            | 291 ms                                                      | 214 ms: 1.36x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.34x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 379 ms: 1.32x faster                                                       |
| async_tree_io              | 731 ms                                                      | 553 ms: 1.32x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 60.4 ms: 1.30x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.28x faster                                                       |
| float                      | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                                      |
| scimark_fft                | 184 ms                                                      | 147 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 395 ms: 1.24x faster                                                       |
| deepcopy                   | 238 us                                                      | 193 us: 1.23x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.10 ms: 1.22x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 40.3 ms: 1.20x faster                                                      |
| pyflate                    | 295 ms                                                      | 251 ms: 1.17x faster                                                       |
| fannkuch                   | 247 ms                                                      | 214 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.2 ms: 1.11x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 54.0 ms: 1.09x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.9 ms: 1.09x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.26 sec: 1.08x faster                                                     |
| pickle_pure_python         | 195 us                                                      | 182 us: 1.07x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 52.6 ms: 1.06x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 484 ms: 1.06x faster                                                       |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 57.2 ns: 1.06x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.94 us: 1.06x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.8 ms: 1.06x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 993 ms: 1.05x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.39 us: 1.05x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.8 ms: 1.04x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 826 us: 1.04x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.04x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 43.4 ms: 1.02x faster                                                      |
| json                       | 3.05 ms                                                     | 2.99 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| raytrace                   | 192 ms                                                      | 190 ms: 1.01x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 81.4 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 95.5 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 138 us: 1.03x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 194 ms: 1.04x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 91.0 ms: 1.04x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 838 us: 1.04x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.96 ms: 1.05x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 95.2 ms: 1.06x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.09 ms: 1.06x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 73.7 ms: 1.07x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.9 ms: 1.07x slower                                                      |
| richards                   | 28.4 ms                                                     | 30.4 ms: 1.07x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                     |
| sympy_sum                  | 91.5 ms                                                     | 98.4 ms: 1.07x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.34 ms: 1.08x slower                                                      |
| async_generators           | 239 ms                                                      | 261 ms: 1.09x slower                                                       |
| richards_super             | 32.1 ms                                                     | 35.0 ms: 1.09x slower                                                      |
| sympy_str                  | 175 ms                                                      | 192 ms: 1.09x slower                                                       |
| 2to3                       | 218 ms                                                      | 242 ms: 1.11x slower                                                       |
| go                         | 91.6 ms                                                     | 102 ms: 1.11x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.61 ms: 1.12x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.85 sec: 1.12x slower                                                     |
| django_template            | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| pycparser                  | 699 ms                                                      | 800 ms: 1.15x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 14.9 ms: 1.15x slower                                                      |
| coverage                   | 40.8 ms                                                     | 47.7 ms: 1.17x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.79 ms: 1.17x slower                                                      |
| sympy_expand               | 284 ms                                                      | 334 ms: 1.18x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 116 us: 1.22x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 925 us: 1.23x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 632 ms: 1.30x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_process, nqueens, generators
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 94.76% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown