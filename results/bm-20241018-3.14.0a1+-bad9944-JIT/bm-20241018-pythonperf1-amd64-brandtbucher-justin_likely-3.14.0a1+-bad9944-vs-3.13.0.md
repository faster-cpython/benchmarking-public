# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_likely
- machine: windows-amd64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.05x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 250 ms: 1.15x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.93 sec: 1.22x slower                                                     |
| tornado_http   | 92.8 ms                                                     | 99.5 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 260 ms: 1.11x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.54 sec: 1.06x faster                                                     |
| async_tree_none_tg         | 206 ms                                                      | 210 ms: 1.02x slower                                                       |
| async_tree_io              | 521 ms                                                      | 554 ms: 1.06x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 399 ms: 1.07x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| async_generators           | 223 ms                                                      | 268 ms: 1.20x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 632 ms: 1.23x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (4): async_tree_none, async_tree_cpu_io_mixed, asyncio_tcp, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 55.0 ms: 1.17x faster                                                      |
| float          | 48.1 ms                                                     | 46.5 ms: 1.03x faster                                                      |
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 14.7 ms                                                     | 14.8 ms: 1.01x slower                                                      |
| regex_dna      | 114 ms                                                      | 117 ms: 1.02x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 92.9 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.29 sec: 1.06x faster                                                     |
| xml_etree_generate   | 53.3 ms                                                     | 51.5 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 63.5 ms: 1.02x slower                                                      |
| pickle               | 7.34 us                                                     | 7.52 us: 1.02x slower                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 95.9 ms: 1.03x slower                                                      |
| unpickle             | 8.63 us                                                     | 8.99 us: 1.04x slower                                                      |
| unpickle_list        | 2.72 us                                                     | 2.87 us: 1.05x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.16 ms: 1.07x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 198 us: 1.08x slower                                                       |
| unpickle_pure_python | 127 us                                                      | 143 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (4): pickle_list, pickle_dict, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.7 ms: 1.05x slower                                                      |
| python_startup         | 22.2 ms                                                     | 24.4 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.13 ms: 1.22x faster                                                      |
| django_template | 21.8 ms                                                     | 27.7 ms: 1.27x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 19.4 ms: 1.30x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 46.0 ms: 1.40x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.18x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 527 us: 16.46x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 16.8 us: 1.30x faster                                                      |
| mako                       | 6.24 ms                                                     | 5.13 ms: 1.22x faster                                                      |
| nbody                      | 64.5 ms                                                     | 55.0 ms: 1.17x faster                                                      |
| deepcopy                   | 223 us                                                      | 194 us: 1.15x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 260 ms: 1.11x faster                                                       |
| scimark_fft                | 174 ms                                                      | 157 ms: 1.11x faster                                                       |
| scimark_sor                | 72.0 ms                                                     | 65.1 ms: 1.11x faster                                                      |
| spectral_norm              | 59.2 ms                                                     | 53.9 ms: 1.10x faster                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 37.1 ms: 1.09x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.88 us: 1.07x faster                                                      |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.54 sec: 1.06x faster                                                     |
| telco                      | 4.85 ms                                                     | 4.56 ms: 1.06x faster                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.29 sec: 1.06x faster                                                     |
| crypto_pyaes               | 42.8 ms                                                     | 40.8 ms: 1.05x faster                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.23 ms: 1.05x faster                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 51.5 ms: 1.04x faster                                                      |
| float                      | 48.1 ms                                                     | 46.5 ms: 1.03x faster                                                      |
| pprint_safe_repr           | 493 ms                                                      | 480 ms: 1.03x faster                                                       |
| pprint_pformat             | 991 ms                                                      | 972 ms: 1.02x faster                                                       |
| fannkuch                   | 245 ms                                                      | 240 ms: 1.02x faster                                                       |
| json                       | 2.98 ms                                                     | 2.95 ms: 1.01x faster                                                      |
| sqlite_synth               | 1.60 us                                                     | 1.59 us: 1.01x faster                                                      |
| pidigits                   | 148 ms                                                      | 147 ms: 1.01x faster                                                       |
| regex_v8                   | 14.7 ms                                                     | 14.8 ms: 1.01x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 63.5 ms: 1.02x slower                                                      |
| async_tree_none_tg         | 206 ms                                                      | 210 ms: 1.02x slower                                                       |
| dulwich_log                | 40.4 ms                                                     | 41.2 ms: 1.02x slower                                                      |
| bench_thread_pool          | 828 us                                                      | 845 us: 1.02x slower                                                       |
| scimark_lu                 | 54.0 ms                                                     | 55.2 ms: 1.02x slower                                                      |
| regex_dna                  | 114 ms                                                      | 117 ms: 1.02x slower                                                       |
| pickle                     | 7.34 us                                                     | 7.52 us: 1.02x slower                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 95.9 ms: 1.03x slower                                                      |
| unpickle                   | 8.63 us                                                     | 8.99 us: 1.04x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 76.0 ms: 1.05x slower                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 18.7 ms: 1.05x slower                                                      |
| coverage                   | 46.7 ms                                                     | 49.2 ms: 1.05x slower                                                      |
| unpickle_list              | 2.72 us                                                     | 2.87 us: 1.05x slower                                                      |
| async_tree_io              | 521 ms                                                      | 554 ms: 1.06x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 399 ms: 1.07x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 6.16 ms: 1.07x slower                                                      |
| tornado_http               | 92.8 ms                                                     | 99.5 ms: 1.07x slower                                                      |
| pyflate                    | 275 ms                                                      | 296 ms: 1.07x slower                                                       |
| pickle_pure_python         | 183 us                                                      | 198 us: 1.08x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.67 us: 1.08x slower                                                      |
| go                         | 84.6 ms                                                     | 92.0 ms: 1.09x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.25 us: 1.09x slower                                                      |
| python_startup             | 22.2 ms                                                     | 24.4 ms: 1.10x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 56.1 ns: 1.10x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.53 sec: 1.11x slower                                                     |
| chaos                      | 37.9 ms                                                     | 42.2 ms: 1.11x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 143 us: 1.13x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 63.7 ms: 1.15x slower                                                      |
| 2to3                       | 217 ms                                                      | 250 ms: 1.15x slower                                                       |
| comprehensions             | 10.2 us                                                     | 11.9 us: 1.16x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 92.9 ms: 1.16x slower                                                      |
| sympy_expand               | 285 ms                                                      | 332 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 100 us                                                      | 118 us: 1.17x slower                                                       |
| sympy_str                  | 166 ms                                                      | 195 ms: 1.18x slower                                                       |
| sqlglot_parse              | 761 us                                                      | 908 us: 1.19x slower                                                       |
| async_generators           | 223 ms                                                      | 268 ms: 1.20x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 104 ms: 1.21x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.93 sec: 1.22x slower                                                     |
| generators                 | 19.5 ms                                                     | 23.9 ms: 1.23x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 632 ms: 1.23x slower                                                       |
| sqlglot_normalize          | 171 ms                                                      | 212 ms: 1.24x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.35 ms: 1.26x slower                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.96 ms: 1.26x slower                                                      |
| django_template            | 21.8 ms                                                     | 27.7 ms: 1.27x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.21 ms: 1.27x slower                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 89.7 ms: 1.29x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 15.9 ms: 1.30x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 19.4 ms: 1.30x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 43.4 ms: 1.31x slower                                                      |
| richards                   | 26.0 ms                                                     | 34.3 ms: 1.32x slower                                                      |
| richards_super             | 29.3 ms                                                     | 38.6 ms: 1.32x slower                                                      |
| pylint                     | 211 ms                                                      | 282 ms: 1.34x slower                                                       |
| raytrace                   | 156 ms                                                      | 213 ms: 1.36x slower                                                       |
| genshi_xml                 | 32.8 ms                                                     | 46.0 ms: 1.40x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 5.25 ms: 1.42x slower                                                      |
| unpack_sequence            | 40.0 ns                                                     | 59.5 ns: 1.49x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 1.41 ms: 1.70x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (12): pickle_list, pycparser, async_tree_none, regex_effbot, async_tree_cpu_io_mixed, asyncio_tcp, pathlib, pickle_dict, xml_etree_process, json_loads, html5lib, async_tree_memoization
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: sphinx

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown