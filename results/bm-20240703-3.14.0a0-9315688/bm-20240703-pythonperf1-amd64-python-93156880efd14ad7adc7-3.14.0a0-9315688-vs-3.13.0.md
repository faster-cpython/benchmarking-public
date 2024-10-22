# Results vs. 3.13.0

- fork: python
- ref: 93156880efd14ad7adc7
- machine: windows-amd64
- commit hash: 9315688
- commit date: 2024-07-03
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 227 ms: 1.05x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.67 sec: 1.06x slower                                                     |
| tornado_http   | 92.8 ms                                                     | 91.1 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 533 ms: 1.23x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 245 ms: 1.17x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 196 ms: 1.05x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 259 ms: 1.05x faster                                                       |
| async_tree_none            | 223 ms                                                      | 214 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 386 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 532 ms: 1.04x slower                                                       |
| async_tree_io              | 521 ms                                                      | 545 ms: 1.05x slower                                                       |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 48.1 ms                                                     | 56.9 ms: 1.18x slower                                                      |
| nbody          | 64.5 ms                                                     | 80.3 ms: 1.25x slower                                                      |
| Geometric mean | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 80.1 ms                                                     | 85.8 ms: 1.07x slower                                                      |
| regex_dna      | 114 ms                                                      | 124 ms: 1.09x slower                                                       |
| regex_v8       | 14.7 ms                                                     | 17.4 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.2 ms                                                     | 92.5 ms: 1.01x faster                                                      |
| json_dumps           | 5.76 ms                                                     | 6.09 ms: 1.06x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 65.9 ms: 1.06x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 59.1 ms: 1.11x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.1 ms: 1.13x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 209 us: 1.14x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.57 sec: 1.15x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 150 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 21.2 ms: 1.05x faster                                                      |
| python_startup_no_site | 17.8 ms                                                     | 17.5 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.8 ms                                                     | 24.4 ms: 1.12x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 37.0 ms: 1.13x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 16.8 ms: 1.13x slower                                                      |
| mako            | 6.24 ms                                                     | 7.52 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 540 us: 16.08x faster                                                      |
| deepcopy                   | 223 us                                                      | 182 us: 1.23x faster                                                       |
| asyncio_tcp                | 654 ms                                                      | 533 ms: 1.23x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 245 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.86 us: 1.09x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 196 ms: 1.05x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 259 ms: 1.05x faster                                                       |
| python_startup             | 22.2 ms                                                     | 21.2 ms: 1.05x faster                                                      |
| async_tree_none            | 223 ms                                                      | 214 ms: 1.04x faster                                                       |
| deepcopy_memo              | 21.8 us                                                     | 21.0 us: 1.04x faster                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 67.8 ms: 1.03x faster                                                      |
| tornado_http               | 92.8 ms                                                     | 91.1 ms: 1.02x faster                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 17.5 ms: 1.01x faster                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 92.5 ms: 1.01x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.57 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 88.7 ms: 1.03x slower                                                      |
| telco                      | 4.85 ms                                                     | 4.97 ms: 1.03x slower                                                      |
| sympy_expand               | 285 ms                                                      | 293 ms: 1.03x slower                                                       |
| mdp                        | 1.38 sec                                                    | 1.43 sec: 1.03x slower                                                     |
| coverage                   | 46.7 ms                                                     | 48.2 ms: 1.03x slower                                                      |
| sympy_str                  | 166 ms                                                      | 171 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 386 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 532 ms: 1.04x slower                                                       |
| async_tree_io              | 521 ms                                                      | 545 ms: 1.05x slower                                                       |
| 2to3                       | 217 ms                                                      | 227 ms: 1.05x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 6.09 ms: 1.06x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 65.9 ms: 1.06x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.67 sec: 1.06x slower                                                     |
| sympy_integrate            | 12.3 ms                                                     | 13.0 ms: 1.06x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 77.0 ms: 1.06x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 35.2 ms: 1.07x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 85.8 ms: 1.07x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 109 us: 1.08x slower                                                       |
| regex_dna                  | 114 ms                                                      | 124 ms: 1.09x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.75 us: 1.10x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 911 us: 1.10x slower                                                       |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 171 ms                                                      | 188 ms: 1.10x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.31 us: 1.10x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 543 ms: 1.10x slower                                                       |
| go                         | 84.6 ms                                                     | 93.5 ms: 1.11x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 59.1 ms: 1.11x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 61.8 ms: 1.11x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.11 sec: 1.12x slower                                                     |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                      |
| pycparser                  | 758 ms                                                      | 848 ms: 1.12x slower                                                       |
| django_template            | 21.8 ms                                                     | 24.4 ms: 1.12x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 41.1 ms: 1.13x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 37.0 ms: 1.13x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 16.8 ms: 1.13x slower                                                      |
| raytrace                   | 156 ms                                                      | 177 ms: 1.13x slower                                                       |
| richards                   | 26.0 ms                                                     | 29.6 ms: 1.14x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 209 us: 1.14x slower                                                       |
| richards_super             | 29.3 ms                                                     | 33.4 ms: 1.14x slower                                                      |
| pyflate                    | 275 ms                                                      | 315 ms: 1.14x slower                                                       |
| generators                 | 19.5 ms                                                     | 22.3 ms: 1.15x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.57 sec: 1.15x slower                                                     |
| comprehensions             | 10.2 us                                                     | 11.8 us: 1.15x slower                                                      |
| chaos                      | 37.9 ms                                                     | 43.6 ms: 1.15x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 68.2 ms: 1.15x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.11 ms: 1.16x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.17 ms: 1.16x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.30 ms: 1.17x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 891 us: 1.17x slower                                                       |
| scimark_sor                | 72.0 ms                                                     | 84.4 ms: 1.17x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 150 us: 1.18x slower                                                       |
| float                      | 48.1 ms                                                     | 56.9 ms: 1.18x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 17.4 ms: 1.18x slower                                                      |
| fannkuch                   | 245 ms                                                      | 291 ms: 1.19x slower                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 51.5 ms: 1.20x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 48.4 ms: 1.20x slower                                                      |
| mako                       | 6.24 ms                                                     | 7.52 ms: 1.21x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 61.8 ns: 1.21x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 65.6 ms: 1.22x slower                                                      |
| scimark_fft                | 174 ms                                                      | 213 ms: 1.22x slower                                                       |
| nbody                      | 64.5 ms                                                     | 80.3 ms: 1.25x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.98 ms: 1.27x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (9): asyncio_tcp_ssl, async_tree_cpu_io_mixed, bench_thread_pool, pathlib, json_loads, regex_effbot, html5lib, pylint, json
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown