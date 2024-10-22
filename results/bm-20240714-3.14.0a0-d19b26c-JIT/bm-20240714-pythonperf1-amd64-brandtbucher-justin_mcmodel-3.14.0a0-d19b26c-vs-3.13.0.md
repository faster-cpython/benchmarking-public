# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_mcmodel
- machine: windows-amd64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.00x faster
- HPT reliability: 98.18%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 234 ms: 1.08x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.78 sec: 1.13x slower                                                     |
| html5lib       | 38.6 ms                                                     | 41.9 ms: 1.09x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 85.4 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 475 ms: 1.38x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 245 ms: 1.18x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.42 sec: 1.15x faster                                                     |
| async_tree_none_tg         | 206 ms                                                      | 190 ms: 1.08x faster                                                       |
| async_tree_none            | 223 ms                                                      | 208 ms: 1.07x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 256 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 384 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 530 ms: 1.03x slower                                                       |
| async_tree_io              | 521 ms                                                      | 543 ms: 1.04x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                      |
| async_generators           | 223 ms                                                      | 259 ms: 1.16x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 51.1 ms: 1.26x faster                                                      |
| float          | 48.1 ms                                                     | 45.1 ms: 1.07x faster                                                      |
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                      |
| regex_dna      | 114 ms                                                      | 120 ms: 1.05x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 90.2 ms: 1.13x slower                                                      |
| regex_v8       | 14.7 ms                                                     | 23.9 ms: 1.63x slower                                                      |
| Geometric mean | (ref)                                                       | 1.17x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.28 sec: 1.06x faster                                                     |
| pickle_pure_python   | 183 us                                                      | 179 us: 1.02x faster                                                       |
| xml_etree_generate   | 53.3 ms                                                     | 52.8 ms: 1.01x faster                                                      |
| json_loads           | 14.3 us                                                     | 14.3 us: 1.00x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 38.1 ms: 1.04x slower                                                      |
| unpickle_pure_python | 127 us                                                      | 134 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 20.9 ms: 1.06x faster                                                      |
| python_startup_no_site | 17.8 ms                                                     | 17.1 ms: 1.04x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.18 ms: 1.20x faster                                                      |
| django_template | 21.8 ms                                                     | 26.3 ms: 1.21x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 18.2 ms: 1.22x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 44.8 ms: 1.37x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 528 us: 16.45x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 15.6 us: 1.40x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 475 ms: 1.38x faster                                                       |
| spectral_norm              | 59.2 ms                                                     | 45.8 ms: 1.29x faster                                                      |
| nbody                      | 64.5 ms                                                     | 51.1 ms: 1.26x faster                                                      |
| deepcopy                   | 223 us                                                      | 180 us: 1.24x faster                                                       |
| mako                       | 6.24 ms                                                     | 5.18 ms: 1.20x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 245 ms: 1.18x faster                                                       |
| scimark_fft                | 174 ms                                                      | 151 ms: 1.16x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.42 sec: 1.15x faster                                                     |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.12x faster                                                      |
| fannkuch                   | 245 ms                                                      | 225 ms: 1.09x faster                                                       |
| tornado_http               | 92.8 ms                                                     | 85.4 ms: 1.09x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 74.9 ms: 1.08x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 190 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.17 ms: 1.08x faster                                                      |
| async_tree_none            | 223 ms                                                      | 208 ms: 1.07x faster                                                       |
| float                      | 48.1 ms                                                     | 45.1 ms: 1.07x faster                                                      |
| pprint_safe_repr           | 493 ms                                                      | 462 ms: 1.07x faster                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.28 sec: 1.06x faster                                                     |
| python_startup             | 22.2 ms                                                     | 20.9 ms: 1.06x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 256 ms: 1.06x faster                                                       |
| pyflate                    | 275 ms                                                      | 260 ms: 1.06x faster                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 38.1 ms: 1.06x faster                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 40.8 ms: 1.05x faster                                                      |
| pprint_pformat             | 991 ms                                                      | 947 ms: 1.05x faster                                                       |
| python_startup_no_site     | 17.8 ms                                                     | 17.1 ms: 1.04x faster                                                      |
| bench_thread_pool          | 828 us                                                      | 808 us: 1.02x faster                                                       |
| pickle_pure_python         | 183 us                                                      | 179 us: 1.02x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 52.8 ms: 1.01x faster                                                      |
| json_loads                 | 14.3 us                                                     | 14.3 us: 1.00x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.56 ms: 1.00x slower                                                      |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| logging_simple             | 5.72 us                                                     | 5.80 us: 1.01x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.27 us: 1.02x slower                                                      |
| telco                      | 4.85 ms                                                     | 4.95 ms: 1.02x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 74.1 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 384 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 530 ms: 1.03x slower                                                       |
| json                       | 2.98 ms                                                     | 3.09 ms: 1.04x slower                                                      |
| coverage                   | 46.7 ms                                                     | 48.5 ms: 1.04x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 38.1 ms: 1.04x slower                                                      |
| async_tree_io              | 521 ms                                                      | 543 ms: 1.04x slower                                                       |
| regex_dna                  | 114 ms                                                      | 120 ms: 1.05x slower                                                       |
| chaos                      | 37.9 ms                                                     | 40.0 ms: 1.05x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.46 sec: 1.06x slower                                                     |
| unpickle_pure_python       | 127 us                                                      | 134 us: 1.06x slower                                                       |
| sqlglot_parse              | 761 us                                                      | 815 us: 1.07x slower                                                       |
| 2to3                       | 217 ms                                                      | 234 ms: 1.08x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 41.9 ms: 1.09x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 900 us: 1.09x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 94.0 ms: 1.09x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.04 ms: 1.09x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 36.4 ms: 1.10x slower                                                      |
| pylint                     | 211 ms                                                      | 232 ms: 1.10x slower                                                       |
| sympy_str                  | 166 ms                                                      | 184 ms: 1.11x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 61.9 ms: 1.12x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 112 us: 1.12x slower                                                       |
| sympy_expand               | 285 ms                                                      | 319 ms: 1.12x slower                                                       |
| logging_silent             | 51.0 ns                                                     | 57.3 ns: 1.12x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 90.2 ms: 1.13x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 193 ms: 1.13x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.78 sec: 1.13x slower                                                     |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 14.0 ms: 1.14x slower                                                      |
| go                         | 84.6 ms                                                     | 97.7 ms: 1.16x slower                                                      |
| async_generators           | 223 ms                                                      | 259 ms: 1.16x slower                                                       |
| richards                   | 26.0 ms                                                     | 30.6 ms: 1.18x slower                                                      |
| raytrace                   | 156 ms                                                      | 185 ms: 1.19x slower                                                       |
| richards_super             | 29.3 ms                                                     | 34.8 ms: 1.19x slower                                                      |
| django_template            | 21.8 ms                                                     | 26.3 ms: 1.21x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 18.2 ms: 1.22x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.61 ms: 1.25x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.35 ms: 1.26x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 91.6 ms: 1.27x slower                                                      |
| generators                 | 19.5 ms                                                     | 25.0 ms: 1.28x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 44.8 ms: 1.37x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 77.0 ms: 1.43x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 23.9 ms: 1.63x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, bench_mp_pool, xml_etree_iterparse, comprehensions, xml_etree_parse, json_dumps, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 98.18% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown