# Results vs. 3.12.0

- fork: python
- ref: 33903c53dbdb768e1ef7
- machine: windows-amd64
- commit hash: 33903c5
- commit date: 2024-07-01
- overall geometric mean: 1.05x faster
- HPT reliability: 95.15%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 234 ms: 1.08x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.77 sec: 1.06x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 83.7 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 190 ms: 1.50x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 247 ms: 1.48x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 528 ms: 1.46x faster                                                       |
| async_tree_none            | 291 ms                                                      | 210 ms: 1.38x faster                                                       |
| async_tree_io              | 731 ms                                                      | 540 ms: 1.35x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 257 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.38x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 50.2 ms: 1.43x faster                                                      |
| float          | 56.8 ms                                                     | 45.7 ms: 1.24x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 88.5 ms: 1.01x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 22.3 ms: 1.57x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 178 us: 1.10x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.27 sec: 1.08x faster                                                     |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.0 ms: 1.07x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 53.4 ms: 1.05x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 135 us: 1.01x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 5.85 ms: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.2 ms: 1.06x slower                                                      |
| python_startup         | 19.5 ms                                                     | 20.8 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.21 ms: 1.36x faster                                                      |
| django_template | 22.9 ms                                                     | 26.2 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 190 ms: 1.50x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 15.9 us: 1.49x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 247 ms: 1.48x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 528 ms: 1.46x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.46 sec: 1.44x faster                                                     |
| nbody                      | 71.9 ms                                                     | 50.2 ms: 1.43x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 46.9 ms: 1.43x faster                                                      |
| async_tree_none            | 291 ms                                                      | 210 ms: 1.38x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.21 ms: 1.36x faster                                                      |
| async_tree_io              | 731 ms                                                      | 540 ms: 1.35x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.34x faster                                                      |
| deepcopy                   | 238 us                                                      | 179 us: 1.33x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 257 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                       |
| float                      | 56.8 ms                                                     | 45.7 ms: 1.24x faster                                                      |
| scimark_fft                | 184 ms                                                      | 152 ms: 1.21x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.14 ms: 1.19x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 41.1 ms: 1.18x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.5 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                                      |
| pyflate                    | 295 ms                                                      | 263 ms: 1.12x faster                                                       |
| fannkuch                   | 247 ms                                                      | 223 ms: 1.11x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 178 us: 1.10x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 787 us: 1.09x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.27 sec: 1.08x faster                                                     |
| logging_format             | 6.72 us                                                     | 6.23 us: 1.08x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.83 us: 1.08x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 83.7 ms: 1.07x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.6 ms: 1.07x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.0 ms: 1.07x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 75.8 ms: 1.06x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 985 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 486 ms: 1.06x faster                                                       |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 53.4 ms: 1.05x faster                                                      |
| raytrace                   | 192 ms                                                      | 185 ms: 1.04x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 472 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| json                       | 3.05 ms                                                     | 2.98 ms: 1.02x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.9 ms: 1.01x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 75.0 ms: 1.00x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 88.5 ms: 1.01x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 135 us: 1.01x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 92.9 ms: 1.01x slower                                                      |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.02x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 823 us: 1.02x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.05 ms: 1.03x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.85 ms: 1.03x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| go                         | 91.6 ms                                                     | 94.7 ms: 1.03x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 194 ms: 1.04x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 36.2 ms: 1.05x slower                                                      |
| richards_super             | 32.1 ms                                                     | 33.9 ms: 1.06x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.2 ms: 1.06x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.77 sec: 1.06x slower                                                     |
| richards                   | 28.4 ms                                                     | 30.3 ms: 1.07x slower                                                      |
| python_startup             | 19.5 ms                                                     | 20.8 ms: 1.07x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.31 ms: 1.07x slower                                                      |
| 2to3                       | 218 ms                                                      | 234 ms: 1.08x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 14.0 ms: 1.08x slower                                                      |
| sympy_expand               | 284 ms                                                      | 307 ms: 1.08x slower                                                       |
| generators                 | 22.5 ms                                                     | 24.5 ms: 1.09x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.54 ms: 1.10x slower                                                      |
| pycparser                  | 699 ms                                                      | 781 ms: 1.12x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 88.6 ms: 1.12x slower                                                      |
| async_generators           | 239 ms                                                      | 272 ms: 1.14x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.2 ms: 1.14x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.69 ms: 1.14x slower                                                      |
| coverage                   | 40.8 ms                                                     | 48.2 ms: 1.18x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 906 us: 1.20x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 116 us: 1.22x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 73.4 ms: 1.25x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 22.3 ms: 1.57x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (3): logging_silent, xml_etree_parse, bench_mp_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240701-3.14.0a0-33903c5-JIT/bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 95.15% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown