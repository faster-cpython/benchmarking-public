# Results vs. base

- fork: python
- ref: v3.13.0b2
- machine: windows-amd64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.04x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:---------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                                                                    | 229 ms: 1.11x slower                                                                                          |
| chameleon      | 4.80 ms                                                                                                   | 5.00 ms: 1.04x slower                                                                                         |
| docutils       | 1.63 sec                                                                                                  | 1.77 sec: 1.09x slower                                                                                        |
| html5lib       | 35.0 ms                                                                                                   | 37.9 ms: 1.08x slower                                                                                         |
| tornado_http   | 81.8 ms                                                                                                   | 86.1 ms: 1.05x slower                                                                                         |
| Geometric mean | (ref)                                                                                                     | 1.07x slower                                                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|---------------------------|:---------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                                                                    | 624 ms: 1.03x slower                                                                                          |
| async_tree_none           | 218 ms                                                                                                    | 227 ms: 1.04x slower                                                                                          |
| async_tree_memoization    | 264 ms                                                                                                    | 278 ms: 1.05x slower                                                                                          |
| async_tree_memoization_tg | 258 ms                                                                                                    | 273 ms: 1.06x slower                                                                                          |
| async_tree_none_tg        | 202 ms                                                                                                    | 215 ms: 1.06x slower                                                                                          |
| Geometric mean            | (ref)                                                                                                     | 1.03x slower                                                                                                  |

Benchmark hidden because not significant (3): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:---------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                                                                   | 53.1 ms: 1.27x faster                                                                                         |
| float          | 49.7 ms                                                                                                   | 44.3 ms: 1.12x faster                                                                                         |
| Geometric mean | (ref)                                                                                                     | 1.13x faster                                                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:---------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                                                                    | 116 ms: 1.03x faster                                                                                          |
| regex_effbot   | 1.58 ms                                                                                                   | 1.55 ms: 1.02x faster                                                                                         |
| regex_compile  | 78.0 ms                                                                                                   | 88.9 ms: 1.14x slower                                                                                         |
| Geometric mean | (ref)                                                                                                     | 1.01x slower                                                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------|:---------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                                                                  | 1.24 sec: 1.09x faster                                                                                        |
| xml_etree_generate   | 53.2 ms                                                                                                   | 51.4 ms: 1.03x faster                                                                                         |
| pickle_dict          | 18.1 us                                                                                                   | 17.6 us: 1.03x faster                                                                                         |
| xml_etree_iterparse  | 62.3 ms                                                                                                   | 61.2 ms: 1.02x faster                                                                                         |
| xml_etree_parse      | 90.9 ms                                                                                                   | 90.3 ms: 1.01x faster                                                                                         |
| json_loads           | 14.2 us                                                                                                   | 14.1 us: 1.01x faster                                                                                         |
| xml_etree_process    | 36.4 ms                                                                                                   | 36.8 ms: 1.01x slower                                                                                         |
| json_dumps           | 5.61 ms                                                                                                   | 5.70 ms: 1.02x slower                                                                                         |
| pickle               | 7.11 us                                                                                                   | 7.27 us: 1.02x slower                                                                                         |
| unpickle             | 8.40 us                                                                                                   | 8.73 us: 1.04x slower                                                                                         |
| unpickle_list        | 2.62 us                                                                                                   | 2.78 us: 1.06x slower                                                                                         |
| unpickle_pure_python | 122 us                                                                                                    | 130 us: 1.07x slower                                                                                          |
| Geometric mean       | (ref)                                                                                                     | 1.00x slower                                                                                                  |

Benchmark hidden because not significant (2): pickle_list, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|------------------------|:---------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                                                                   | 22.7 ms: 1.12x slower                                                                                         |
| python_startup_no_site | 16.2 ms                                                                                                   | 18.6 ms: 1.15x slower                                                                                         |
| Geometric mean         | (ref)                                                                                                     | 1.13x slower                                                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|-----------------|:---------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                                                                   | 5.13 ms: 1.24x faster                                                                                         |
| django_template | 21.7 ms                                                                                                   | 25.4 ms: 1.17x slower                                                                                         |
| genshi_text     | 14.4 ms                                                                                                   | 17.9 ms: 1.25x slower                                                                                         |
| genshi_xml      | 31.6 ms                                                                                                   | 44.2 ms: 1.40x slower                                                                                         |
| Geometric mean  | (ref)                                                                                                     | 1.13x slower                                                                                                  |

All benchmarks:
===============

| Benchmark                 | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|---------------------------|:---------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|
| spectral_norm             | 63.7 ms                                                                                                   | 45.3 ms: 1.41x faster                                                                                         |
| nbody                     | 67.6 ms                                                                                                   | 53.1 ms: 1.27x faster                                                                                         |
| mako                      | 6.36 ms                                                                                                   | 5.13 ms: 1.24x faster                                                                                         |
| scimark_sparse_mat_mult   | 2.50 ms                                                                                                   | 2.19 ms: 1.14x faster                                                                                         |
| scimark_fft               | 171 ms                                                                                                    | 150 ms: 1.14x faster                                                                                          |
| fannkuch                  | 243 ms                                                                                                    | 215 ms: 1.13x faster                                                                                          |
| float                     | 49.7 ms                                                                                                   | 44.3 ms: 1.12x faster                                                                                         |
| json                      | 3.19 ms                                                                                                   | 2.88 ms: 1.11x faster                                                                                         |
| crypto_pyaes              | 45.5 ms                                                                                                   | 41.5 ms: 1.10x faster                                                                                         |
| tomli_loads               | 1.35 sec                                                                                                  | 1.24 sec: 1.09x faster                                                                                        |
| pyflate                   | 279 ms                                                                                                    | 257 ms: 1.08x faster                                                                                          |
| deepcopy_memo             | 22.1 us                                                                                                   | 20.9 us: 1.05x faster                                                                                         |
| telco                     | 4.67 ms                                                                                                   | 4.46 ms: 1.05x faster                                                                                         |
| scimark_monte_carlo       | 39.1 ms                                                                                                   | 37.7 ms: 1.04x faster                                                                                         |
| xml_etree_generate        | 53.2 ms                                                                                                   | 51.4 ms: 1.03x faster                                                                                         |
| pickle_dict               | 18.1 us                                                                                                   | 17.6 us: 1.03x faster                                                                                         |
| pprint_safe_repr          | 474 ms                                                                                                    | 461 ms: 1.03x faster                                                                                          |
| regex_dna                 | 119 ms                                                                                                    | 116 ms: 1.03x faster                                                                                          |
| pprint_pformat            | 966 ms                                                                                                    | 946 ms: 1.02x faster                                                                                          |
| regex_effbot              | 1.58 ms                                                                                                   | 1.55 ms: 1.02x faster                                                                                         |
| xml_etree_iterparse       | 62.3 ms                                                                                                   | 61.2 ms: 1.02x faster                                                                                         |
| xml_etree_parse           | 90.9 ms                                                                                                   | 90.3 ms: 1.01x faster                                                                                         |
| json_loads                | 14.2 us                                                                                                   | 14.1 us: 1.01x faster                                                                                         |
| pathlib                   | 75.9 ms                                                                                                   | 76.3 ms: 1.01x slower                                                                                         |
| xml_etree_process         | 36.4 ms                                                                                                   | 36.8 ms: 1.01x slower                                                                                         |
| json_dumps                | 5.61 ms                                                                                                   | 5.70 ms: 1.02x slower                                                                                         |
| chaos                     | 38.4 ms                                                                                                   | 39.2 ms: 1.02x slower                                                                                         |
| pickle                    | 7.11 us                                                                                                   | 7.27 us: 1.02x slower                                                                                         |
| logging_simple            | 5.78 us                                                                                                   | 5.91 us: 1.02x slower                                                                                         |
| create_gc_cycles          | 888 us                                                                                                    | 912 us: 1.03x slower                                                                                          |
| logging_format            | 6.22 us                                                                                                   | 6.42 us: 1.03x slower                                                                                         |
| meteor_contest            | 69.9 ms                                                                                                   | 72.0 ms: 1.03x slower                                                                                         |
| async_tree_io_tg          | 605 ms                                                                                                    | 624 ms: 1.03x slower                                                                                          |
| bench_thread_pool         | 768 us                                                                                                    | 793 us: 1.03x slower                                                                                          |
| coroutines                | 12.8 ms                                                                                                   | 13.2 ms: 1.04x slower                                                                                         |
| unpickle                  | 8.40 us                                                                                                   | 8.73 us: 1.04x slower                                                                                         |
| chameleon                 | 4.80 ms                                                                                                   | 5.00 ms: 1.04x slower                                                                                         |
| async_tree_none           | 218 ms                                                                                                    | 227 ms: 1.04x slower                                                                                          |
| logging_silent            | 52.9 ns                                                                                                   | 55.3 ns: 1.05x slower                                                                                         |
| tornado_http              | 81.8 ms                                                                                                   | 86.1 ms: 1.05x slower                                                                                         |
| async_tree_memoization    | 264 ms                                                                                                    | 278 ms: 1.05x slower                                                                                          |
| async_tree_memoization_tg | 258 ms                                                                                                    | 273 ms: 1.06x slower                                                                                          |
| dulwich_log               | 38.0 ms                                                                                                   | 40.2 ms: 1.06x slower                                                                                         |
| sqlite_synth              | 1.60 us                                                                                                   | 1.69 us: 1.06x slower                                                                                         |
| unpickle_list             | 2.62 us                                                                                                   | 2.78 us: 1.06x slower                                                                                         |
| async_tree_none_tg        | 202 ms                                                                                                    | 215 ms: 1.06x slower                                                                                          |
| deepcopy_reduce           | 1.99 us                                                                                                   | 2.13 us: 1.07x slower                                                                                         |
| unpickle_pure_python      | 122 us                                                                                                    | 130 us: 1.07x slower                                                                                          |
| sqlglot_parse             | 748 us                                                                                                    | 801 us: 1.07x slower                                                                                          |
| aiohttp                   | 889 us                                                                                                    | 954 us: 1.07x slower                                                                                          |
| coverage                  | 42.1 ms                                                                                                   | 45.5 ms: 1.08x slower                                                                                         |
| nqueens                   | 56.7 ms                                                                                                   | 61.4 ms: 1.08x slower                                                                                         |
| html5lib                  | 35.0 ms                                                                                                   | 37.9 ms: 1.08x slower                                                                                         |
| generators                | 19.6 ms                                                                                                   | 21.2 ms: 1.08x slower                                                                                         |
| raytrace                  | 162 ms                                                                                                    | 176 ms: 1.09x slower                                                                                          |
| sqlglot_transpile         | 955 us                                                                                                    | 1.04 ms: 1.09x slower                                                                                         |
| docutils                  | 1.63 sec                                                                                                  | 1.77 sec: 1.09x slower                                                                                        |
| deepcopy                  | 220 us                                                                                                    | 241 us: 1.10x slower                                                                                          |
| scimark_sor               | 75.3 ms                                                                                                   | 83.5 ms: 1.11x slower                                                                                         |
| 2to3                      | 207 ms                                                                                                    | 229 ms: 1.11x slower                                                                                          |
| richards                  | 26.7 ms                                                                                                   | 29.7 ms: 1.11x slower                                                                                         |
| bench_mp_pool             | 64.8 ms                                                                                                   | 72.0 ms: 1.11x slower                                                                                         |
| richards_super            | 30.2 ms                                                                                                   | 33.5 ms: 1.11x slower                                                                                         |
| sympy_sum                 | 84.4 ms                                                                                                   | 93.9 ms: 1.11x slower                                                                                         |
| python_startup            | 20.3 ms                                                                                                   | 22.7 ms: 1.12x slower                                                                                         |
| typing_runtime_protocols  | 101 us                                                                                                    | 113 us: 1.12x slower                                                                                          |
| async_generators          | 223 ms                                                                                                    | 252 ms: 1.13x slower                                                                                          |
| sqlglot_optimize          | 32.7 ms                                                                                                   | 37.0 ms: 1.13x slower                                                                                         |
| thrift                    | 8.11 ms                                                                                                   | 9.21 ms: 1.14x slower                                                                                         |
| sympy_str                 | 159 ms                                                                                                    | 181 ms: 1.14x slower                                                                                          |
| regex_compile             | 78.0 ms                                                                                                   | 88.9 ms: 1.14x slower                                                                                         |
| go                        | 82.1 ms                                                                                                   | 93.8 ms: 1.14x slower                                                                                         |
| pylint                    | 205 ms                                                                                                    | 235 ms: 1.15x slower                                                                                          |
| python_startup_no_site    | 16.2 ms                                                                                                   | 18.6 ms: 1.15x slower                                                                                         |
| mdp                       | 1.31 sec                                                                                                  | 1.51 sec: 1.15x slower                                                                                        |
| sympy_integrate           | 12.2 ms                                                                                                   | 14.1 ms: 1.15x slower                                                                                         |
| mypy2                     | 418 ms                                                                                                    | 486 ms: 1.16x slower                                                                                          |
| django_template           | 21.7 ms                                                                                                   | 25.4 ms: 1.17x slower                                                                                         |
| sympy_expand              | 271 ms                                                                                                    | 317 ms: 1.17x slower                                                                                          |
| scimark_lu                | 56.6 ms                                                                                                   | 69.4 ms: 1.23x slower                                                                                         |
| genshi_text               | 14.4 ms                                                                                                   | 17.9 ms: 1.25x slower                                                                                         |
| deltablue                 | 1.88 ms                                                                                                   | 2.37 ms: 1.26x slower                                                                                         |
| hexiom                    | 3.72 ms                                                                                                   | 4.72 ms: 1.27x slower                                                                                         |
| genshi_xml                | 31.6 ms                                                                                                   | 44.2 ms: 1.40x slower                                                                                         |
| Geometric mean            | (ref)                                                                                                     | 1.04x slower                                                                                                  |

Benchmark hidden because not significant (13): regex_v8, asyncio_tcp_ssl, pickle_list, pycparser, async_tree_io, pidigits, gc_traversal, pickle_pure_python, flaskblogging, comprehensions, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_tcp
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: sqlglot_normalize

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown