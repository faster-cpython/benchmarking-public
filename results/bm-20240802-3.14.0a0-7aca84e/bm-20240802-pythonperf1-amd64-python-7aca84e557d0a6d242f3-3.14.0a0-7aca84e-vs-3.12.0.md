# Results vs. 3.12.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-amd64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.04x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 236 ms: 1.08x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.79 sec: 1.08x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 95.3 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 252 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.41x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 559 ms: 1.38x faster                                                       |
| async_tree_none            | 291 ms                                                      | 223 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 396 ms: 1.27x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 270 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                       |
| async_tree_io              | 731 ms                                                      | 597 ms: 1.22x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.32x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 85.4 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 94.5 ms: 1.08x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.8 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 94.8 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.6 ms: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 58.7 ms: 1.05x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.26 ms: 1.10x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 42.1 ms: 1.12x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 221 us: 1.13x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 153 us: 1.15x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.62 sec: 1.18x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 252 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.41x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 559 ms: 1.38x faster                                                       |
| async_tree_none            | 291 ms                                                      | 223 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 396 ms: 1.27x faster                                                       |
| deepcopy                   | 238 us                                                      | 189 us: 1.26x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.67 sec: 1.26x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 270 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                       |
| async_tree_io              | 731 ms                                                      | 597 ms: 1.22x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.7 us: 1.15x faster                                                      |
| comprehensions             | 14.1 us                                                     | 12.5 us: 1.13x faster                                                      |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.96 us: 1.07x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.8 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 837 us: 1.02x faster                                                       |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 44.5 ms: 1.01x slower                                                      |
| pathlib                    | 80.5 ms                                                     | 81.5 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 94.8 ms: 1.02x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.6 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.62 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 94.0 ms: 1.03x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 77.2 ms: 1.03x slower                                                      |
| chaos                      | 43.3 ms                                                     | 44.9 ms: 1.04x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.52 us: 1.04x slower                                                      |
| sympy_str                  | 175 ms                                                      | 182 ms: 1.04x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                      |
| logging_format             | 6.72 us                                                     | 7.01 us: 1.04x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 65.5 ms: 1.04x slower                                                      |
| async_generators           | 239 ms                                                      | 252 ms: 1.05x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 58.7 ms: 1.05x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 95.3 ms: 1.06x slower                                                      |
| raytrace                   | 192 ms                                                      | 206 ms: 1.07x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 52.0 ms: 1.07x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 94.5 ms: 1.08x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.79 sec: 1.08x slower                                                     |
| logging_silent             | 60.5 ns                                                     | 65.5 ns: 1.08x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 203 ms: 1.08x slower                                                       |
| 2to3                       | 218 ms                                                      | 236 ms: 1.08x slower                                                       |
| scimark_fft                | 184 ms                                                      | 202 ms: 1.09x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 37.8 ms: 1.09x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.37 ms: 1.10x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.26 ms: 1.10x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.13 ms: 1.10x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 64.8 ms: 1.10x slower                                                      |
| sympy_expand               | 284 ms                                                      | 314 ms: 1.11x slower                                                       |
| go                         | 91.6 ms                                                     | 101 ms: 1.11x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 74.7 ms: 1.12x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 42.1 ms: 1.12x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 903 us: 1.12x slower                                                       |
| pyflate                    | 295 ms                                                      | 332 ms: 1.13x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 221 us: 1.13x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 581 ms: 1.13x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.18 sec: 1.13x slower                                                     |
| django_template            | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.70 ms: 1.15x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 153 us: 1.15x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                                     |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.4 ms: 1.15x slower                                                      |
| coverage                   | 40.8 ms                                                     | 47.2 ms: 1.16x slower                                                      |
| pycparser                  | 699 ms                                                      | 811 ms: 1.16x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 16.8 ms: 1.18x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.62 sec: 1.18x slower                                                     |
| nbody                      | 71.9 ms                                                     | 85.4 ms: 1.19x slower                                                      |
| fannkuch                   | 247 ms                                                      | 296 ms: 1.20x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 912 us: 1.21x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 116 us: 1.21x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 95.8 ms: 1.22x slower                                                      |
| richards                   | 28.4 ms                                                     | 34.7 ms: 1.22x slower                                                      |
| richards_super             | 32.1 ms                                                     | 39.3 ms: 1.22x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.13 ms: 1.24x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 637 ms: 1.31x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (3): mako, float, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown