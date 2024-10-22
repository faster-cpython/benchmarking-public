# Results vs. 3.13.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: windows-amd64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.04x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 253 ms: 1.16x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.95 sec: 1.24x slower                                                     |
| html5lib       | 38.6 ms                                                     | 41.7 ms: 1.08x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 98.2 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 262 ms: 1.10x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.54 sec: 1.06x faster                                                     |
| async_tree_none            | 223 ms                                                      | 217 ms: 1.03x faster                                                       |
| asyncio_tcp                | 654 ms                                                      | 673 ms: 1.03x slower                                                       |
| async_tree_memoization     | 271 ms                                                      | 282 ms: 1.04x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 401 ms: 1.07x slower                                                       |
| async_tree_io              | 521 ms                                                      | 565 ms: 1.08x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 574 ms: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| async_generators           | 223 ms                                                      | 260 ms: 1.17x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 49.4 ms: 1.31x faster                                                      |
| float          | 48.1 ms                                                     | 47.2 ms: 1.02x faster                                                      |
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| regex_v8       | 14.7 ms                                                     | 14.8 ms: 1.01x slower                                                      |
| regex_dna      | 114 ms                                                      | 117 ms: 1.03x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 95.7 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_list          | 2.89 us                                                     | 2.72 us: 1.06x faster                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 50.5 ms: 1.06x faster                                                      |
| tomli_loads          | 1.36 sec                                                    | 1.30 sec: 1.04x faster                                                     |
| pickle_dict          | 18.0 us                                                     | 17.8 us: 1.01x faster                                                      |
| pickle               | 7.34 us                                                     | 7.24 us: 1.01x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 63.0 ms: 1.01x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 5.84 ms: 1.01x slower                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 95.8 ms: 1.03x slower                                                      |
| unpickle             | 8.63 us                                                     | 8.94 us: 1.04x slower                                                      |
| unpickle_list        | 2.72 us                                                     | 2.83 us: 1.04x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 198 us: 1.08x slower                                                       |
| unpickle_pure_python | 127 us                                                      | 147 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.5 ms: 1.04x slower                                                      |
| python_startup         | 22.2 ms                                                     | 24.3 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 4.99 ms: 1.25x faster                                                      |
| django_template | 21.8 ms                                                     | 26.9 ms: 1.23x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 19.1 ms: 1.29x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 47.3 ms: 1.44x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.16x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 523 us: 16.58x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 16.2 us: 1.35x faster                                                      |
| nbody                      | 64.5 ms                                                     | 49.4 ms: 1.31x faster                                                      |
| mako                       | 6.24 ms                                                     | 4.99 ms: 1.25x faster                                                      |
| deepcopy                   | 223 us                                                      | 186 us: 1.20x faster                                                       |
| scimark_sor                | 72.0 ms                                                     | 61.9 ms: 1.16x faster                                                      |
| scimark_fft                | 174 ms                                                      | 153 ms: 1.14x faster                                                       |
| spectral_norm              | 59.2 ms                                                     | 52.6 ms: 1.13x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.11 ms: 1.11x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 262 ms: 1.10x faster                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 36.6 ms: 1.10x faster                                                      |
| pprint_safe_repr           | 493 ms                                                      | 450 ms: 1.09x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.46 ms: 1.09x faster                                                      |
| pprint_pformat             | 991 ms                                                      | 923 ms: 1.07x faster                                                       |
| pickle_list                | 2.89 us                                                     | 2.72 us: 1.06x faster                                                      |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.54 sec: 1.06x faster                                                     |
| xml_etree_generate         | 53.3 ms                                                     | 50.5 ms: 1.06x faster                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 40.6 ms: 1.06x faster                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.30 sec: 1.04x faster                                                     |
| async_tree_none            | 223 ms                                                      | 217 ms: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| float                      | 48.1 ms                                                     | 47.2 ms: 1.02x faster                                                      |
| pickle_dict                | 18.0 us                                                     | 17.8 us: 1.01x faster                                                      |
| pickle                     | 7.34 us                                                     | 7.24 us: 1.01x faster                                                      |
| pidigits                   | 148 ms                                                      | 147 ms: 1.01x faster                                                       |
| sqlite_synth               | 1.60 us                                                     | 1.59 us: 1.01x faster                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 63.0 ms: 1.01x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 14.8 ms: 1.01x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 5.84 ms: 1.01x slower                                                      |
| regex_dna                  | 114 ms                                                      | 117 ms: 1.03x slower                                                       |
| xml_etree_parse            | 93.2 ms                                                     | 95.8 ms: 1.03x slower                                                      |
| asyncio_tcp                | 654 ms                                                      | 673 ms: 1.03x slower                                                       |
| scimark_lu                 | 54.0 ms                                                     | 55.7 ms: 1.03x slower                                                      |
| unpickle                   | 8.63 us                                                     | 8.94 us: 1.04x slower                                                      |
| fannkuch                   | 245 ms                                                      | 254 ms: 1.04x slower                                                       |
| async_tree_memoization     | 271 ms                                                      | 282 ms: 1.04x slower                                                       |
| unpickle_list              | 2.72 us                                                     | 2.83 us: 1.04x slower                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 18.5 ms: 1.04x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 75.4 ms: 1.04x slower                                                      |
| tornado_http               | 92.8 ms                                                     | 98.2 ms: 1.06x slower                                                      |
| coverage                   | 46.7 ms                                                     | 49.6 ms: 1.06x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 43.2 ms: 1.07x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 401 ms: 1.07x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.15 us: 1.07x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.63 us: 1.08x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 198 us: 1.08x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 41.7 ms: 1.08x slower                                                      |
| async_tree_io              | 521 ms                                                      | 565 ms: 1.08x slower                                                       |
| go                         | 84.6 ms                                                     | 91.9 ms: 1.09x slower                                                      |
| chaos                      | 37.9 ms                                                     | 41.5 ms: 1.10x slower                                                      |
| python_startup             | 22.2 ms                                                     | 24.3 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 111 us: 1.10x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 574 ms: 1.12x slower                                                       |
| pyflate                    | 275 ms                                                      | 310 ms: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| comprehensions             | 10.2 us                                                     | 11.6 us: 1.13x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 58.2 ns: 1.14x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 147 us: 1.16x slower                                                       |
| mdp                        | 1.38 sec                                                    | 1.61 sec: 1.16x slower                                                     |
| 2to3                       | 217 ms                                                      | 253 ms: 1.16x slower                                                       |
| sqlglot_parse              | 761 us                                                      | 887 us: 1.17x slower                                                       |
| async_generators           | 223 ms                                                      | 260 ms: 1.17x slower                                                       |
| sympy_expand               | 285 ms                                                      | 334 ms: 1.17x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 65.1 ms: 1.17x slower                                                      |
| sympy_str                  | 166 ms                                                      | 196 ms: 1.18x slower                                                       |
| generators                 | 19.5 ms                                                     | 23.2 ms: 1.19x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 95.7 ms: 1.19x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 205 ms: 1.20x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 104 ms: 1.20x slower                                                       |
| sqlglot_transpile          | 952 us                                                      | 1.17 ms: 1.23x slower                                                      |
| django_template            | 21.8 ms                                                     | 26.9 ms: 1.23x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.95 sec: 1.24x slower                                                     |
| gc_traversal               | 1.55 ms                                                     | 1.93 ms: 1.24x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.34 ms: 1.25x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 15.6 ms: 1.27x slower                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 88.9 ms: 1.28x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 19.1 ms: 1.29x slower                                                      |
| raytrace                   | 156 ms                                                      | 202 ms: 1.30x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 42.9 ms: 1.30x slower                                                      |
| richards_super             | 29.3 ms                                                     | 38.6 ms: 1.32x slower                                                      |
| pylint                     | 211 ms                                                      | 279 ms: 1.33x slower                                                       |
| richards                   | 26.0 ms                                                     | 34.5 ms: 1.33x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 5.28 ms: 1.43x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 47.3 ms: 1.44x slower                                                      |
| unpack_sequence            | 40.0 ns                                                     | 58.5 ns: 1.46x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 1.38 ms: 1.67x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_cpu_io_mixed, xml_etree_process, json_loads, pycparser, pathlib, bench_thread_pool, json
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: sphinx

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown