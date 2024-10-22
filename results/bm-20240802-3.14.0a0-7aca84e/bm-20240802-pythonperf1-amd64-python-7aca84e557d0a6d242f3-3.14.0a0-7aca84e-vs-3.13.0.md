# Results vs. 3.13.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-amd64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 236 ms: 1.09x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.79 sec: 1.14x slower                                                     |
| html5lib       | 38.6 ms                                                     | 42.0 ms: 1.09x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 95.3 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.14x faster                                                       |
| asyncio_tcp                | 654 ms                                                      | 637 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 394 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 396 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 559 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| async_generators           | 223 ms                                                      | 252 ms: 1.13x slower                                                       |
| async_tree_io              | 521 ms                                                      | 597 ms: 1.15x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_memoization, async_tree_none, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 48.1 ms                                                     | 57.0 ms: 1.18x slower                                                      |
| nbody          | 64.5 ms                                                     | 85.4 ms: 1.32x slower                                                      |
| Geometric mean | (ref)                                                       | 1.17x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_v8       | 14.7 ms                                                     | 16.8 ms: 1.14x slower                                                      |
| regex_compile  | 80.1 ms                                                     | 94.5 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 14.3 us: 1.00x faster                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 94.8 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 66.6 ms: 1.07x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.26 ms: 1.09x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 58.7 ms: 1.10x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 42.1 ms: 1.15x slower                                                      |
| tomli_loads          | 1.36 sec                                                    | 1.62 sec: 1.19x slower                                                     |
| pickle_pure_python   | 183 us                                                      | 221 us: 1.20x slower                                                       |
| unpickle_pure_python | 127 us                                                      | 153 us: 1.21x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 7.06 ms: 1.13x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 37.4 ms: 1.14x slower                                                      |
| django_template | 21.8 ms                                                     | 26.1 ms: 1.20x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.8 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.17x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 524 us: 16.56x faster                                                      |
| deepcopy                   | 223 us                                                      | 189 us: 1.18x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.14x faster                                                       |
| deepcopy_memo              | 21.8 us                                                     | 20.7 us: 1.06x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.96 us: 1.03x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 637 ms: 1.03x faster                                                       |
| json_loads                 | 14.3 us                                                     | 14.3 us: 1.00x faster                                                      |
| json                       | 2.98 ms                                                     | 3.01 ms: 1.01x slower                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.57 ms: 1.01x slower                                                      |
| coverage                   | 46.7 ms                                                     | 47.2 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 94.8 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 394 ms: 1.02x slower                                                       |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| tornado_http               | 92.8 ms                                                     | 95.3 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 396 ms: 1.06x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.13 ms: 1.06x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 77.2 ms: 1.07x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 66.6 ms: 1.07x slower                                                      |
| pycparser                  | 758 ms                                                      | 811 ms: 1.07x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 42.0 ms: 1.09x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 6.26 ms: 1.09x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 94.0 ms: 1.09x slower                                                      |
| 2to3                       | 217 ms                                                      | 236 ms: 1.09x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 559 ms: 1.09x slower                                                       |
| sympy_str                  | 166 ms                                                      | 182 ms: 1.09x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 912 us: 1.10x slower                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 58.7 ms: 1.10x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                                      |
| sympy_expand               | 285 ms                                                      | 314 ms: 1.10x slower                                                       |
| pylint                     | 211 ms                                                      | 232 ms: 1.10x slower                                                       |
| dulwich_log                | 40.4 ms                                                     | 44.5 ms: 1.10x slower                                                      |
| generators                 | 19.5 ms                                                     | 21.8 ms: 1.12x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.62 ms: 1.12x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| async_generators           | 223 ms                                                      | 252 ms: 1.13x slower                                                       |
| mako                       | 6.24 ms                                                     | 7.06 ms: 1.13x slower                                                      |
| logging_format             | 6.15 us                                                     | 7.01 us: 1.14x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.52 us: 1.14x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.79 sec: 1.14x slower                                                     |
| mdp                        | 1.38 sec                                                    | 1.58 sec: 1.14x slower                                                     |
| genshi_xml                 | 32.8 ms                                                     | 37.4 ms: 1.14x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 37.8 ms: 1.14x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 16.8 ms: 1.14x slower                                                      |
| async_tree_io              | 521 ms                                                      | 597 ms: 1.15x slower                                                       |
| typing_runtime_protocols   | 100 us                                                      | 116 us: 1.15x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 42.1 ms: 1.15x slower                                                      |
| scimark_fft                | 174 ms                                                      | 202 ms: 1.16x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 94.5 ms: 1.18x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 581 ms: 1.18x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 65.5 ms: 1.18x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.13 ms: 1.18x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 203 ms: 1.18x slower                                                       |
| float                      | 48.1 ms                                                     | 57.0 ms: 1.18x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 903 us: 1.19x slower                                                       |
| chaos                      | 37.9 ms                                                     | 44.9 ms: 1.19x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.62 sec: 1.19x slower                                                     |
| pprint_pformat             | 991 ms                                                      | 1.18 sec: 1.19x slower                                                     |
| go                         | 84.6 ms                                                     | 101 ms: 1.20x slower                                                       |
| django_template            | 21.8 ms                                                     | 26.1 ms: 1.20x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 17.8 ms: 1.20x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 64.8 ms: 1.20x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 221 us: 1.20x slower                                                       |
| pyflate                    | 275 ms                                                      | 332 ms: 1.21x slower                                                       |
| unpickle_pure_python       | 127 us                                                      | 153 us: 1.21x slower                                                       |
| fannkuch                   | 245 ms                                                      | 296 ms: 1.21x slower                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 52.0 ms: 1.21x slower                                                      |
| comprehensions             | 10.2 us                                                     | 12.5 us: 1.22x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 50.4 ms: 1.25x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 74.7 ms: 1.26x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.37 ms: 1.27x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.70 ms: 1.27x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 65.5 ns: 1.28x slower                                                      |
| raytrace                   | 156 ms                                                      | 206 ms: 1.32x slower                                                       |
| nbody                      | 64.5 ms                                                     | 85.4 ms: 1.32x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 95.8 ms: 1.33x slower                                                      |
| richards                   | 26.0 ms                                                     | 34.7 ms: 1.33x slower                                                      |
| richards_super             | 29.3 ms                                                     | 39.3 ms: 1.34x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (10): async_tree_none_tg, async_tree_memoization, async_tree_none, bench_mp_pool, python_startup, regex_dna, python_startup_no_site, pathlib, bench_thread_pool, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown