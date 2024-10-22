# Results vs. 3.13.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-amd64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 224 ms: 1.03x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.68 sec: 1.07x slower                                                     |
| html5lib       | 38.6 ms                                                     | 40.3 ms: 1.04x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 81.5 ms: 1.14x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 474 ms: 1.38x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 244 ms: 1.18x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 191 ms: 1.08x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 255 ms: 1.07x faster                                                       |
| async_tree_none            | 223 ms                                                      | 212 ms: 1.05x faster                                                       |
| async_tree_io              | 521 ms                                                      | 536 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 528 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 387 ms: 1.03x slower                                                       |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.01x slower                                                       |
| float          | 48.1 ms                                                     | 56.5 ms: 1.18x slower                                                      |
| nbody          | 64.5 ms                                                     | 78.5 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| regex_dna      | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 89.0 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 14.2 us: 1.01x faster                                                      |
| json_dumps           | 5.76 ms                                                     | 5.97 ms: 1.04x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 66.5 ms: 1.07x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 58.0 ms: 1.09x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 40.6 ms: 1.11x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 204 us: 1.11x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.57 sec: 1.15x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 150 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 21.1 ms: 1.05x faster                                                      |
| python_startup_no_site | 17.8 ms                                                     | 17.4 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.8 ms                                                     | 23.9 ms: 1.10x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 16.4 ms: 1.11x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 37.2 ms: 1.14x slower                                                      |
| mako            | 6.24 ms                                                     | 7.37 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 522 us: 16.64x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 474 ms: 1.38x faster                                                       |
| deepcopy                   | 223 us                                                      | 181 us: 1.23x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 244 ms: 1.18x faster                                                       |
| tornado_http               | 92.8 ms                                                     | 81.5 ms: 1.14x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 74.1 ms: 1.10x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.86 us: 1.09x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 191 ms: 1.08x faster                                                       |
| bench_mp_pool              | 69.6 ms                                                     | 65.2 ms: 1.07x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 255 ms: 1.07x faster                                                       |
| async_tree_none            | 223 ms                                                      | 212 ms: 1.05x faster                                                       |
| python_startup             | 22.2 ms                                                     | 21.1 ms: 1.05x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 20.8 us: 1.05x faster                                                      |
| bench_thread_pool          | 828 us                                                      | 793 us: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 17.4 ms: 1.02x faster                                                      |
| coverage                   | 46.7 ms                                                     | 46.2 ms: 1.01x faster                                                      |
| json                       | 2.98 ms                                                     | 2.95 ms: 1.01x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.54 ms: 1.01x faster                                                      |
| json_loads                 | 14.3 us                                                     | 14.2 us: 1.01x faster                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.01x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 88.6 ms: 1.03x slower                                                      |
| async_tree_io              | 521 ms                                                      | 536 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 528 ms: 1.03x slower                                                       |
| 2to3                       | 217 ms                                                      | 224 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 387 ms: 1.03x slower                                                       |
| sympy_expand               | 285 ms                                                      | 296 ms: 1.04x slower                                                       |
| regex_dna                  | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 5.97 ms: 1.04x slower                                                      |
| sympy_str                  | 166 ms                                                      | 173 ms: 1.04x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 40.3 ms: 1.04x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 75.7 ms: 1.05x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 34.7 ms: 1.05x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.0 ms: 1.06x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 106 us: 1.06x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.68 sec: 1.07x slower                                                     |
| xml_etree_iterparse        | 62.3 ms                                                     | 66.5 ms: 1.07x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.60 us: 1.07x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 896 us: 1.08x slower                                                       |
| sqlglot_normalize          | 171 ms                                                      | 185 ms: 1.08x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.21 us: 1.09x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 58.0 ms: 1.09x slower                                                      |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                      |
| django_template            | 21.8 ms                                                     | 23.9 ms: 1.10x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.53 sec: 1.10x slower                                                     |
| genshi_text                | 14.9 ms                                                     | 16.4 ms: 1.11x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 546 ms: 1.11x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 89.0 ms: 1.11x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 40.6 ms: 1.11x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 204 us: 1.11x slower                                                       |
| pprint_pformat             | 991 ms                                                      | 1.10 sec: 1.11x slower                                                     |
| pyflate                    | 275 ms                                                      | 309 ms: 1.12x slower                                                       |
| comprehensions             | 10.2 us                                                     | 11.6 us: 1.13x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 62.9 ms: 1.13x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 37.2 ms: 1.14x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.08 ms: 1.14x slower                                                      |
| generators                 | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| go                         | 84.6 ms                                                     | 97.0 ms: 1.15x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.57 sec: 1.15x slower                                                     |
| sqlglot_parse              | 761 us                                                      | 878 us: 1.15x slower                                                       |
| raytrace                   | 156 ms                                                      | 181 ms: 1.16x slower                                                       |
| chaos                      | 37.9 ms                                                     | 44.0 ms: 1.16x slower                                                      |
| float                      | 48.1 ms                                                     | 56.5 ms: 1.18x slower                                                      |
| richards_super             | 29.3 ms                                                     | 34.6 ms: 1.18x slower                                                      |
| richards                   | 26.0 ms                                                     | 30.7 ms: 1.18x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 150 us: 1.18x slower                                                       |
| mako                       | 6.24 ms                                                     | 7.37 ms: 1.18x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.21 ms: 1.18x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 52.0 ms: 1.21x slower                                                      |
| nbody                      | 64.5 ms                                                     | 78.5 ms: 1.22x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.51 ms: 1.22x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 72.4 ms: 1.22x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 66.2 ms: 1.23x slower                                                      |
| scimark_fft                | 174 ms                                                      | 216 ms: 1.24x slower                                                       |
| fannkuch                   | 245 ms                                                      | 304 ms: 1.24x slower                                                       |
| logging_silent             | 51.0 ns                                                     | 63.5 ns: 1.24x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.93 ms: 1.25x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 90.7 ms: 1.26x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 52.0 ms: 1.29x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (7): asyncio_tcp_ssl, async_tree_cpu_io_mixed, pylint, xml_etree_parse, telco, pycparser, regex_v8
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown