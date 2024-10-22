# Results vs. 3.13.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-amd64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.00x slower
- HPT reliability: 99.76%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 241 ms: 1.11x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.91 sec: 1.22x slower                                                     |
| html5lib       | 38.6 ms                                                     | 42.0 ms: 1.09x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 97.7 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 523 ms: 1.25x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.13x faster                                                       |
| async_tree_none            | 223 ms                                                      | 201 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 195 ms: 1.05x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 258 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 393 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 393 ms: 1.05x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 555 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| async_tree_io              | 521 ms                                                      | 584 ms: 1.12x slower                                                       |
| async_generators           | 223 ms                                                      | 264 ms: 1.18x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 49.0 ms: 1.32x faster                                                      |
| float          | 48.1 ms                                                     | 43.8 ms: 1.10x faster                                                      |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 14.7 ms                                                     | 15.2 ms: 1.04x slower                                                      |
| regex_dna      | 114 ms                                                      | 124 ms: 1.08x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 95.2 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.24 sec: 1.10x faster                                                     |
| xml_etree_generate   | 53.3 ms                                                     | 49.0 ms: 1.09x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 34.7 ms: 1.05x faster                                                      |
| pickle               | 7.34 us                                                     | 7.17 us: 1.02x faster                                                      |
| pickle_dict          | 18.0 us                                                     | 17.7 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 61.5 ms: 1.01x faster                                                      |
| json_loads           | 14.3 us                                                     | 14.3 us: 1.00x faster                                                      |
| json_dumps           | 5.76 ms                                                     | 5.86 ms: 1.02x slower                                                      |
| unpickle_list        | 2.72 us                                                     | 2.80 us: 1.03x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 194 us: 1.06x slower                                                       |
| unpickle             | 8.63 us                                                     | 9.18 us: 1.06x slower                                                      |
| unpickle_pure_python | 127 us                                                      | 141 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (2): pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.5 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.15 ms: 1.21x faster                                                      |
| django_template | 21.8 ms                                                     | 26.1 ms: 1.20x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 18.7 ms: 1.26x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 44.0 ms: 1.34x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 520 us: 16.69x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 15.2 us: 1.44x faster                                                      |
| nbody                      | 64.5 ms                                                     | 49.0 ms: 1.32x faster                                                      |
| spectral_norm              | 59.2 ms                                                     | 45.6 ms: 1.30x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 523 ms: 1.25x faster                                                       |
| mako                       | 6.24 ms                                                     | 5.15 ms: 1.21x faster                                                      |
| scimark_sor                | 72.0 ms                                                     | 59.9 ms: 1.20x faster                                                      |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                       |
| scimark_fft                | 174 ms                                                      | 148 ms: 1.18x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.12x faster                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 38.3 ms: 1.12x faster                                                      |
| async_tree_none            | 223 ms                                                      | 201 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.12 ms: 1.10x faster                                                      |
| float                      | 48.1 ms                                                     | 43.8 ms: 1.10x faster                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.24 sec: 1.10x faster                                                     |
| xml_etree_generate         | 53.3 ms                                                     | 49.0 ms: 1.09x faster                                                      |
| pycparser                  | 758 ms                                                      | 706 ms: 1.07x faster                                                       |
| pyflate                    | 275 ms                                                      | 261 ms: 1.06x faster                                                       |
| fannkuch                   | 245 ms                                                      | 232 ms: 1.06x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 34.7 ms: 1.05x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 195 ms: 1.05x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 258 ms: 1.05x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.64 ms: 1.04x faster                                                      |
| scimark_lu                 | 54.0 ms                                                     | 52.3 ms: 1.03x faster                                                      |
| pickle                     | 7.34 us                                                     | 7.17 us: 1.02x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 79.5 ms: 1.02x faster                                                      |
| deltablue                  | 1.86 ms                                                     | 1.83 ms: 1.02x faster                                                      |
| pickle_dict                | 18.0 us                                                     | 17.7 us: 1.02x faster                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 61.5 ms: 1.01x faster                                                      |
| json_loads                 | 14.3 us                                                     | 14.3 us: 1.00x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.56 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 393 ms: 1.02x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 5.86 ms: 1.02x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 503 ms: 1.02x slower                                                       |
| unpickle_list              | 2.72 us                                                     | 2.80 us: 1.03x slower                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 71.6 ms: 1.03x slower                                                      |
| comprehensions             | 10.2 us                                                     | 10.6 us: 1.03x slower                                                      |
| coverage                   | 46.7 ms                                                     | 48.2 ms: 1.03x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 15.2 ms: 1.04x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 75.1 ms: 1.04x slower                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 18.5 ms: 1.04x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.03 sec: 1.04x slower                                                     |
| logging_simple             | 5.72 us                                                     | 5.97 us: 1.04x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.43 us: 1.05x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 42.1 ms: 1.05x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 393 ms: 1.05x slower                                                       |
| tornado_http               | 92.8 ms                                                     | 97.7 ms: 1.05x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 194 us: 1.06x slower                                                       |
| unpickle                   | 8.63 us                                                     | 9.18 us: 1.06x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 43.0 ms: 1.06x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.6 ms: 1.07x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.49 sec: 1.08x slower                                                     |
| typing_runtime_protocols   | 100 us                                                      | 108 us: 1.08x slower                                                       |
| go                         | 84.6 ms                                                     | 91.4 ms: 1.08x slower                                                      |
| regex_dna                  | 114 ms                                                      | 124 ms: 1.08x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 555 ms: 1.08x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 42.0 ms: 1.09x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 60.5 ms: 1.09x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 914 us: 1.10x slower                                                       |
| 2to3                       | 217 ms                                                      | 241 ms: 1.11x slower                                                       |
| unpickle_pure_python       | 127 us                                                      | 141 us: 1.11x slower                                                       |
| async_tree_io              | 521 ms                                                      | 584 ms: 1.12x slower                                                       |
| logging_silent             | 51.0 ns                                                     | 57.3 ns: 1.12x slower                                                      |
| sympy_str                  | 166 ms                                                      | 188 ms: 1.13x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 97.8 ms: 1.13x slower                                                      |
| sympy_expand               | 285 ms                                                      | 329 ms: 1.15x slower                                                       |
| sqlglot_parse              | 761 us                                                      | 883 us: 1.16x slower                                                       |
| sqlglot_normalize          | 171 ms                                                      | 200 ms: 1.17x slower                                                       |
| generators                 | 19.5 ms                                                     | 22.8 ms: 1.17x slower                                                      |
| async_generators           | 223 ms                                                      | 264 ms: 1.18x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 95.2 ms: 1.19x slower                                                      |
| django_template            | 21.8 ms                                                     | 26.1 ms: 1.20x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 14.8 ms: 1.20x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 39.8 ms: 1.21x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.15 ms: 1.21x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.91 sec: 1.22x slower                                                     |
| genshi_text                | 14.9 ms                                                     | 18.7 ms: 1.26x slower                                                      |
| raytrace                   | 156 ms                                                      | 196 ms: 1.26x slower                                                       |
| pylint                     | 211 ms                                                      | 266 ms: 1.26x slower                                                       |
| richards_super             | 29.3 ms                                                     | 38.4 ms: 1.31x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.92 ms: 1.33x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 44.0 ms: 1.34x slower                                                      |
| richards                   | 26.0 ms                                                     | 35.8 ms: 1.38x slower                                                      |
| unpack_sequence            | 40.0 ns                                                     | 58.4 ns: 1.46x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (8): asyncio_tcp_ssl, pickle_list, bench_thread_pool, xml_etree_parse, json, sqlite_synth, regex_effbot, python_startup
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 99.76% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown