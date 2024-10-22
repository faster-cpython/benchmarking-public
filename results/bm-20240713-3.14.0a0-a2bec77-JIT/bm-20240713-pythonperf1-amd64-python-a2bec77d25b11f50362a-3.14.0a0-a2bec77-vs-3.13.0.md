# Results vs. 3.13.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-amd64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.02x faster
- HPT reliability: 90.67%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 233 ms: 1.07x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.77 sec: 1.12x slower                                                     |
| html5lib       | 38.6 ms                                                     | 39.9 ms: 1.03x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 84.3 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 465 ms: 1.41x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 241 ms: 1.19x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.44 sec: 1.14x faster                                                     |
| async_tree_none_tg         | 206 ms                                                      | 186 ms: 1.11x faster                                                       |
| async_tree_none            | 223 ms                                                      | 205 ms: 1.09x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 250 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 385 ms: 1.03x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| async_generators           | 223 ms                                                      | 257 ms: 1.15x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 51.0 ms: 1.26x faster                                                      |
| float          | 48.1 ms                                                     | 45.1 ms: 1.07x faster                                                      |
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_dna      | 114 ms                                                      | 121 ms: 1.06x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 90.5 ms: 1.13x slower                                                      |
| regex_v8       | 14.7 ms                                                     | 20.8 ms: 1.42x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.25 sec: 1.09x faster                                                     |
| pickle_pure_python   | 183 us                                                      | 173 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 62.3 ms                                                     | 60.7 ms: 1.03x faster                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 92.3 ms: 1.01x faster                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 52.8 ms: 1.01x faster                                                      |
| json_dumps           | 5.76 ms                                                     | 5.86 ms: 1.02x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 37.4 ms: 1.02x slower                                                      |
| unpickle_pure_python | 127 us                                                      | 130 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 21.0 ms: 1.05x faster                                                      |
| python_startup_no_site | 17.8 ms                                                     | 17.5 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.16 ms: 1.21x faster                                                      |
| django_template | 21.8 ms                                                     | 25.6 ms: 1.17x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 18.1 ms: 1.22x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 45.2 ms: 1.38x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 519 us: 16.73x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 465 ms: 1.41x faster                                                       |
| deepcopy_memo              | 21.8 us                                                     | 15.8 us: 1.38x faster                                                      |
| spectral_norm              | 59.2 ms                                                     | 45.5 ms: 1.30x faster                                                      |
| nbody                      | 64.5 ms                                                     | 51.0 ms: 1.26x faster                                                      |
| deepcopy                   | 223 us                                                      | 181 us: 1.23x faster                                                       |
| mako                       | 6.24 ms                                                     | 5.16 ms: 1.21x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 241 ms: 1.19x faster                                                       |
| scimark_fft                | 174 ms                                                      | 151 ms: 1.16x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.44 sec: 1.14x faster                                                     |
| deepcopy_reduce            | 2.02 us                                                     | 1.79 us: 1.13x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 186 ms: 1.11x faster                                                       |
| fannkuch                   | 245 ms                                                      | 221 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.12 ms: 1.10x faster                                                      |
| tornado_http               | 92.8 ms                                                     | 84.3 ms: 1.10x faster                                                      |
| async_tree_none            | 223 ms                                                      | 205 ms: 1.09x faster                                                       |
| pathlib                    | 81.2 ms                                                     | 74.6 ms: 1.09x faster                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.25 sec: 1.09x faster                                                     |
| async_tree_memoization     | 271 ms                                                      | 250 ms: 1.08x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.48 ms: 1.08x faster                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 37.6 ms: 1.07x faster                                                      |
| pyflate                    | 275 ms                                                      | 258 ms: 1.07x faster                                                       |
| float                      | 48.1 ms                                                     | 45.1 ms: 1.07x faster                                                      |
| pprint_safe_repr           | 493 ms                                                      | 464 ms: 1.06x faster                                                       |
| pickle_pure_python         | 183 us                                                      | 173 us: 1.06x faster                                                       |
| python_startup             | 22.2 ms                                                     | 21.0 ms: 1.05x faster                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 40.7 ms: 1.05x faster                                                      |
| pprint_pformat             | 991 ms                                                      | 953 ms: 1.04x faster                                                       |
| bench_thread_pool          | 828 us                                                      | 804 us: 1.03x faster                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 60.7 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 17.5 ms: 1.02x faster                                                      |
| coverage                   | 46.7 ms                                                     | 46.1 ms: 1.01x faster                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 92.3 ms: 1.01x faster                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 52.8 ms: 1.01x faster                                                      |
| logging_format             | 6.15 us                                                     | 6.19 us: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| comprehensions             | 10.2 us                                                     | 10.4 us: 1.01x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 5.86 ms: 1.02x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 73.6 ms: 1.02x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 37.4 ms: 1.02x slower                                                      |
| chaos                      | 37.9 ms                                                     | 38.8 ms: 1.02x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 130 us: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 385 ms: 1.03x slower                                                       |
| mdp                        | 1.38 sec                                                    | 1.42 sec: 1.03x slower                                                     |
| json                       | 2.98 ms                                                     | 3.07 ms: 1.03x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 39.9 ms: 1.03x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 804 us: 1.06x slower                                                       |
| regex_dna                  | 114 ms                                                      | 121 ms: 1.06x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 92.9 ms: 1.07x slower                                                      |
| 2to3                       | 217 ms                                                      | 233 ms: 1.07x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 35.6 ms: 1.08x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 59.9 ms: 1.08x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.03 ms: 1.08x slower                                                      |
| pycparser                  | 758 ms                                                      | 822 ms: 1.08x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 901 us: 1.09x slower                                                       |
| sympy_str                  | 166 ms                                                      | 181 ms: 1.09x slower                                                       |
| pylint                     | 211 ms                                                      | 231 ms: 1.09x slower                                                       |
| sympy_expand               | 285 ms                                                      | 313 ms: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 190 ms: 1.11x slower                                                       |
| go                         | 84.6 ms                                                     | 94.2 ms: 1.11x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 56.8 ns: 1.11x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.77 sec: 1.12x slower                                                     |
| typing_runtime_protocols   | 100 us                                                      | 113 us: 1.13x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 90.5 ms: 1.13x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 14.0 ms: 1.14x slower                                                      |
| raytrace                   | 156 ms                                                      | 179 ms: 1.14x slower                                                       |
| async_generators           | 223 ms                                                      | 257 ms: 1.15x slower                                                       |
| richards_super             | 29.3 ms                                                     | 34.0 ms: 1.16x slower                                                      |
| django_template            | 21.8 ms                                                     | 25.6 ms: 1.17x slower                                                      |
| richards                   | 26.0 ms                                                     | 30.6 ms: 1.17x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.25 ms: 1.21x slower                                                      |
| generators                 | 19.5 ms                                                     | 23.6 ms: 1.21x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 18.1 ms: 1.22x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 88.9 ms: 1.24x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.62 ms: 1.25x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 70.3 ms: 1.30x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 45.2 ms: 1.38x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 20.8 ms: 1.42x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, gc_traversal, json_loads, bench_mp_pool, logging_simple, async_tree_io, async_tree_io_tg
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 90.67% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown