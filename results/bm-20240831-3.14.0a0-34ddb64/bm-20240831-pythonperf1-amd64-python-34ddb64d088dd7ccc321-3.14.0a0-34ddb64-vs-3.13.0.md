# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-amd64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 226 ms: 1.04x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.69 sec: 1.07x slower                                                     |
| html5lib       | 38.6 ms                                                     | 40.7 ms: 1.05x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 93.8 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 512 ms: 1.28x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 250 ms: 1.15x faster                                                       |
| async_tree_none            | 223 ms                                                      | 210 ms: 1.06x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 260 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 399 ms: 1.07x slower                                                       |
| async_tree_io              | 521 ms                                                      | 573 ms: 1.10x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 564 ms: 1.10x slower                                                       |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.12x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 152 ms: 1.02x slower                                                       |
| float          | 48.1 ms                                                     | 56.2 ms: 1.17x slower                                                      |
| nbody          | 64.5 ms                                                     | 83.6 ms: 1.30x slower                                                      |
| Geometric mean | (ref)                                                       | 1.16x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                      |
| regex_dna      | 114 ms                                                      | 116 ms: 1.01x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 91.5 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.2 ms                                                     | 95.6 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 65.0 ms: 1.04x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 57.7 ms: 1.08x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.24 ms: 1.08x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 40.9 ms: 1.12x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 208 us: 1.14x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.59 sec: 1.17x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 149 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.0 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 6.87 ms: 1.10x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 36.3 ms: 1.11x slower                                                      |
| django_template | 21.8 ms                                                     | 24.2 ms: 1.11x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 16.5 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 525 us: 16.53x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 512 ms: 1.28x faster                                                       |
| deepcopy                   | 223 us                                                      | 186 us: 1.20x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 250 ms: 1.15x faster                                                       |
| deepcopy_memo              | 21.8 us                                                     | 19.5 us: 1.12x faster                                                      |
| async_tree_none            | 223 ms                                                      | 210 ms: 1.06x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.90 us: 1.06x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 260 ms: 1.04x faster                                                       |
| pathlib                    | 81.2 ms                                                     | 79.4 ms: 1.02x faster                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 68.7 ms: 1.01x faster                                                      |
| tornado_http               | 92.8 ms                                                     | 93.8 ms: 1.01x slower                                                      |
| regex_dna                  | 114 ms                                                      | 116 ms: 1.01x slower                                                       |
| python_startup_no_site     | 17.8 ms                                                     | 18.0 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 152 ms: 1.02x slower                                                       |
| xml_etree_parse            | 93.2 ms                                                     | 95.6 ms: 1.03x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.43 sec: 1.04x slower                                                     |
| 2to3                       | 217 ms                                                      | 226 ms: 1.04x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 90.1 ms: 1.04x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 65.0 ms: 1.04x slower                                                      |
| json                       | 2.98 ms                                                     | 3.12 ms: 1.05x slower                                                      |
| telco                      | 4.85 ms                                                     | 5.09 ms: 1.05x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 40.7 ms: 1.05x slower                                                      |
| coverage                   | 46.7 ms                                                     | 49.3 ms: 1.06x slower                                                      |
| generators                 | 19.5 ms                                                     | 20.6 ms: 1.06x slower                                                      |
| sympy_str                  | 166 ms                                                      | 177 ms: 1.06x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 399 ms: 1.07x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.1 ms: 1.07x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.69 sec: 1.07x slower                                                     |
| sympy_expand               | 285 ms                                                      | 307 ms: 1.08x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.63 us: 1.08x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 57.7 ms: 1.08x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 6.24 ms: 1.08x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 78.3 ms: 1.08x slower                                                      |
| pylint                     | 211 ms                                                      | 228 ms: 1.08x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.25 us: 1.09x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 36.3 ms: 1.10x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 44.4 ms: 1.10x slower                                                      |
| async_tree_io              | 521 ms                                                      | 573 ms: 1.10x slower                                                       |
| mako                       | 6.24 ms                                                     | 6.87 ms: 1.10x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 564 ms: 1.10x slower                                                       |
| genshi_xml                 | 32.8 ms                                                     | 36.3 ms: 1.11x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 917 us: 1.11x slower                                                       |
| django_template            | 21.8 ms                                                     | 24.2 ms: 1.11x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 16.5 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 47.8 ms: 1.12x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 191 ms: 1.12x slower                                                       |
| pprint_pformat             | 991 ms                                                      | 1.11 sec: 1.12x slower                                                     |
| xml_etree_process          | 36.5 ms                                                     | 40.9 ms: 1.12x slower                                                      |
| scimark_fft                | 174 ms                                                      | 195 ms: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.12x slower                                                      |
| chaos                      | 37.9 ms                                                     | 42.7 ms: 1.13x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 555 ms: 1.13x slower                                                       |
| pickle_pure_python         | 183 us                                                      | 208 us: 1.14x slower                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.66 ms: 1.14x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 67.4 ms: 1.14x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 91.5 ms: 1.14x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 115 us: 1.14x slower                                                       |
| scimark_lu                 | 54.0 ms                                                     | 62.3 ms: 1.15x slower                                                      |
| comprehensions             | 10.2 us                                                     | 11.8 us: 1.15x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.11 ms: 1.16x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.59 sec: 1.17x slower                                                     |
| float                      | 48.1 ms                                                     | 56.2 ms: 1.17x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.32 ms: 1.17x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 891 us: 1.17x slower                                                       |
| pyflate                    | 275 ms                                                      | 322 ms: 1.17x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 65.2 ms: 1.17x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 149 us: 1.18x slower                                                       |
| fannkuch                   | 245 ms                                                      | 291 ms: 1.19x slower                                                       |
| raytrace                   | 156 ms                                                      | 188 ms: 1.20x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.25 ms: 1.21x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 49.1 ms: 1.22x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 62.5 ns: 1.22x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 88.7 ms: 1.23x slower                                                      |
| richards_super             | 29.3 ms                                                     | 36.2 ms: 1.24x slower                                                      |
| richards                   | 26.0 ms                                                     | 32.4 ms: 1.24x slower                                                      |
| nbody                      | 64.5 ms                                                     | 83.6 ms: 1.30x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (10): asyncio_tcp_ssl, async_tree_none_tg, gc_traversal, python_startup, go, pycparser, json_loads, bench_thread_pool, async_tree_cpu_io_mixed, regex_v8
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown