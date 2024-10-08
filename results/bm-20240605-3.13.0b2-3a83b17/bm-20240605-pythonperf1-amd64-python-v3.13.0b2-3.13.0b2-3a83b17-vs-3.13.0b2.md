# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0b2
- machine: windows-amd64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.04x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:-------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| 2to3           | 229 ms                                                                                                        | 207 ms: 1.11x faster                                                                                      |
| chameleon      | 5.00 ms                                                                                                       | 4.80 ms: 1.04x faster                                                                                     |
| docutils       | 1.77 sec                                                                                                      | 1.63 sec: 1.09x faster                                                                                    |
| html5lib       | 37.9 ms                                                                                                       | 35.0 ms: 1.08x faster                                                                                     |
| tornado_http   | 86.1 ms                                                                                                       | 81.8 ms: 1.05x faster                                                                                     |
| Geometric mean | (ref)                                                                                                         | 1.07x faster                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|---------------------------|:-------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg        | 215 ms                                                                                                        | 202 ms: 1.06x faster                                                                                      |
| async_tree_memoization_tg | 273 ms                                                                                                        | 258 ms: 1.06x faster                                                                                      |
| async_tree_memoization    | 278 ms                                                                                                        | 264 ms: 1.05x faster                                                                                      |
| async_tree_none           | 227 ms                                                                                                        | 218 ms: 1.04x faster                                                                                      |
| async_tree_io_tg          | 624 ms                                                                                                        | 605 ms: 1.03x faster                                                                                      |
| Geometric mean            | (ref)                                                                                                         | 1.03x faster                                                                                              |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:-------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| float          | 44.3 ms                                                                                                       | 49.7 ms: 1.12x slower                                                                                     |
| nbody          | 53.1 ms                                                                                                       | 67.6 ms: 1.27x slower                                                                                     |
| Geometric mean | (ref)                                                                                                         | 1.13x slower                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:-------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| regex_compile  | 88.9 ms                                                                                                       | 78.0 ms: 1.14x faster                                                                                     |
| regex_effbot   | 1.55 ms                                                                                                       | 1.58 ms: 1.02x slower                                                                                     |
| regex_dna      | 116 ms                                                                                                        | 119 ms: 1.03x slower                                                                                      |
| Geometric mean | (ref)                                                                                                         | 1.01x faster                                                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                                                                        | 122 us: 1.07x faster                                                                                      |
| unpickle_list        | 2.78 us                                                                                                       | 2.62 us: 1.06x faster                                                                                     |
| unpickle             | 8.73 us                                                                                                       | 8.40 us: 1.04x faster                                                                                     |
| pickle               | 7.27 us                                                                                                       | 7.11 us: 1.02x faster                                                                                     |
| json_dumps           | 5.70 ms                                                                                                       | 5.61 ms: 1.02x faster                                                                                     |
| xml_etree_process    | 36.8 ms                                                                                                       | 36.4 ms: 1.01x faster                                                                                     |
| json_loads           | 14.1 us                                                                                                       | 14.2 us: 1.01x slower                                                                                     |
| xml_etree_parse      | 90.3 ms                                                                                                       | 90.9 ms: 1.01x slower                                                                                     |
| xml_etree_iterparse  | 61.2 ms                                                                                                       | 62.3 ms: 1.02x slower                                                                                     |
| pickle_dict          | 17.6 us                                                                                                       | 18.1 us: 1.03x slower                                                                                     |
| xml_etree_generate   | 51.4 ms                                                                                                       | 53.2 ms: 1.03x slower                                                                                     |
| tomli_loads          | 1.24 sec                                                                                                      | 1.35 sec: 1.09x slower                                                                                    |
| Geometric mean       | (ref)                                                                                                         | 1.00x faster                                                                                              |

Benchmark hidden because not significant (2): pickle_pure_python, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.6 ms                                                                                                       | 16.2 ms: 1.15x faster                                                                                     |
| python_startup         | 22.7 ms                                                                                                       | 20.3 ms: 1.12x faster                                                                                     |
| Geometric mean         | (ref)                                                                                                         | 1.13x faster                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 44.2 ms                                                                                                       | 31.6 ms: 1.40x faster                                                                                     |
| genshi_text     | 17.9 ms                                                                                                       | 14.4 ms: 1.25x faster                                                                                     |
| django_template | 25.4 ms                                                                                                       | 21.7 ms: 1.17x faster                                                                                     |
| mako            | 5.13 ms                                                                                                       | 6.36 ms: 1.24x slower                                                                                     |
| Geometric mean  | (ref)                                                                                                         | 1.13x faster                                                                                              |

All benchmarks:
===============

| Benchmark                 | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|---------------------------|:-------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| genshi_xml                | 44.2 ms                                                                                                       | 31.6 ms: 1.40x faster                                                                                     |
| hexiom                    | 4.72 ms                                                                                                       | 3.72 ms: 1.27x faster                                                                                     |
| deltablue                 | 2.37 ms                                                                                                       | 1.88 ms: 1.26x faster                                                                                     |
| genshi_text               | 17.9 ms                                                                                                       | 14.4 ms: 1.25x faster                                                                                     |
| scimark_lu                | 69.4 ms                                                                                                       | 56.6 ms: 1.23x faster                                                                                     |
| sympy_expand              | 317 ms                                                                                                        | 271 ms: 1.17x faster                                                                                      |
| django_template           | 25.4 ms                                                                                                       | 21.7 ms: 1.17x faster                                                                                     |
| mypy2                     | 486 ms                                                                                                        | 418 ms: 1.16x faster                                                                                      |
| sympy_integrate           | 14.1 ms                                                                                                       | 12.2 ms: 1.15x faster                                                                                     |
| mdp                       | 1.51 sec                                                                                                      | 1.31 sec: 1.15x faster                                                                                    |
| python_startup_no_site    | 18.6 ms                                                                                                       | 16.2 ms: 1.15x faster                                                                                     |
| pylint                    | 235 ms                                                                                                        | 205 ms: 1.15x faster                                                                                      |
| go                        | 93.8 ms                                                                                                       | 82.1 ms: 1.14x faster                                                                                     |
| regex_compile             | 88.9 ms                                                                                                       | 78.0 ms: 1.14x faster                                                                                     |
| sympy_str                 | 181 ms                                                                                                        | 159 ms: 1.14x faster                                                                                      |
| thrift                    | 9.21 ms                                                                                                       | 8.11 ms: 1.14x faster                                                                                     |
| sqlglot_optimize          | 37.0 ms                                                                                                       | 32.7 ms: 1.13x faster                                                                                     |
| async_generators          | 252 ms                                                                                                        | 223 ms: 1.13x faster                                                                                      |
| typing_runtime_protocols  | 113 us                                                                                                        | 101 us: 1.12x faster                                                                                      |
| python_startup            | 22.7 ms                                                                                                       | 20.3 ms: 1.12x faster                                                                                     |
| sympy_sum                 | 93.9 ms                                                                                                       | 84.4 ms: 1.11x faster                                                                                     |
| richards_super            | 33.5 ms                                                                                                       | 30.2 ms: 1.11x faster                                                                                     |
| bench_mp_pool             | 72.0 ms                                                                                                       | 64.8 ms: 1.11x faster                                                                                     |
| richards                  | 29.7 ms                                                                                                       | 26.7 ms: 1.11x faster                                                                                     |
| 2to3                      | 229 ms                                                                                                        | 207 ms: 1.11x faster                                                                                      |
| scimark_sor               | 83.5 ms                                                                                                       | 75.3 ms: 1.11x faster                                                                                     |
| deepcopy                  | 241 us                                                                                                        | 220 us: 1.10x faster                                                                                      |
| docutils                  | 1.77 sec                                                                                                      | 1.63 sec: 1.09x faster                                                                                    |
| sqlglot_transpile         | 1.04 ms                                                                                                       | 955 us: 1.09x faster                                                                                      |
| raytrace                  | 176 ms                                                                                                        | 162 ms: 1.09x faster                                                                                      |
| generators                | 21.2 ms                                                                                                       | 19.6 ms: 1.08x faster                                                                                     |
| html5lib                  | 37.9 ms                                                                                                       | 35.0 ms: 1.08x faster                                                                                     |
| nqueens                   | 61.4 ms                                                                                                       | 56.7 ms: 1.08x faster                                                                                     |
| coverage                  | 45.5 ms                                                                                                       | 42.1 ms: 1.08x faster                                                                                     |
| aiohttp                   | 954 us                                                                                                        | 889 us: 1.07x faster                                                                                      |
| sqlglot_parse             | 801 us                                                                                                        | 748 us: 1.07x faster                                                                                      |
| unpickle_pure_python      | 130 us                                                                                                        | 122 us: 1.07x faster                                                                                      |
| deepcopy_reduce           | 2.13 us                                                                                                       | 1.99 us: 1.07x faster                                                                                     |
| async_tree_none_tg        | 215 ms                                                                                                        | 202 ms: 1.06x faster                                                                                      |
| unpickle_list             | 2.78 us                                                                                                       | 2.62 us: 1.06x faster                                                                                     |
| sqlite_synth              | 1.69 us                                                                                                       | 1.60 us: 1.06x faster                                                                                     |
| dulwich_log               | 40.2 ms                                                                                                       | 38.0 ms: 1.06x faster                                                                                     |
| async_tree_memoization_tg | 273 ms                                                                                                        | 258 ms: 1.06x faster                                                                                      |
| async_tree_memoization    | 278 ms                                                                                                        | 264 ms: 1.05x faster                                                                                      |
| tornado_http              | 86.1 ms                                                                                                       | 81.8 ms: 1.05x faster                                                                                     |
| logging_silent            | 55.3 ns                                                                                                       | 52.9 ns: 1.05x faster                                                                                     |
| async_tree_none           | 227 ms                                                                                                        | 218 ms: 1.04x faster                                                                                      |
| chameleon                 | 5.00 ms                                                                                                       | 4.80 ms: 1.04x faster                                                                                     |
| unpickle                  | 8.73 us                                                                                                       | 8.40 us: 1.04x faster                                                                                     |
| coroutines                | 13.2 ms                                                                                                       | 12.8 ms: 1.04x faster                                                                                     |
| bench_thread_pool         | 793 us                                                                                                        | 768 us: 1.03x faster                                                                                      |
| async_tree_io_tg          | 624 ms                                                                                                        | 605 ms: 1.03x faster                                                                                      |
| meteor_contest            | 72.0 ms                                                                                                       | 69.9 ms: 1.03x faster                                                                                     |
| logging_format            | 6.42 us                                                                                                       | 6.22 us: 1.03x faster                                                                                     |
| create_gc_cycles          | 912 us                                                                                                        | 888 us: 1.03x faster                                                                                      |
| logging_simple            | 5.91 us                                                                                                       | 5.78 us: 1.02x faster                                                                                     |
| pickle                    | 7.27 us                                                                                                       | 7.11 us: 1.02x faster                                                                                     |
| chaos                     | 39.2 ms                                                                                                       | 38.4 ms: 1.02x faster                                                                                     |
| json_dumps                | 5.70 ms                                                                                                       | 5.61 ms: 1.02x faster                                                                                     |
| xml_etree_process         | 36.8 ms                                                                                                       | 36.4 ms: 1.01x faster                                                                                     |
| pathlib                   | 76.3 ms                                                                                                       | 75.9 ms: 1.01x faster                                                                                     |
| json_loads                | 14.1 us                                                                                                       | 14.2 us: 1.01x slower                                                                                     |
| xml_etree_parse           | 90.3 ms                                                                                                       | 90.9 ms: 1.01x slower                                                                                     |
| xml_etree_iterparse       | 61.2 ms                                                                                                       | 62.3 ms: 1.02x slower                                                                                     |
| regex_effbot              | 1.55 ms                                                                                                       | 1.58 ms: 1.02x slower                                                                                     |
| pprint_pformat            | 946 ms                                                                                                        | 966 ms: 1.02x slower                                                                                      |
| regex_dna                 | 116 ms                                                                                                        | 119 ms: 1.03x slower                                                                                      |
| pprint_safe_repr          | 461 ms                                                                                                        | 474 ms: 1.03x slower                                                                                      |
| pickle_dict               | 17.6 us                                                                                                       | 18.1 us: 1.03x slower                                                                                     |
| xml_etree_generate        | 51.4 ms                                                                                                       | 53.2 ms: 1.03x slower                                                                                     |
| scimark_monte_carlo       | 37.7 ms                                                                                                       | 39.1 ms: 1.04x slower                                                                                     |
| telco                     | 4.46 ms                                                                                                       | 4.67 ms: 1.05x slower                                                                                     |
| deepcopy_memo             | 20.9 us                                                                                                       | 22.1 us: 1.05x slower                                                                                     |
| pyflate                   | 257 ms                                                                                                        | 279 ms: 1.08x slower                                                                                      |
| tomli_loads               | 1.24 sec                                                                                                      | 1.35 sec: 1.09x slower                                                                                    |
| crypto_pyaes              | 41.5 ms                                                                                                       | 45.5 ms: 1.10x slower                                                                                     |
| json                      | 2.88 ms                                                                                                       | 3.19 ms: 1.11x slower                                                                                     |
| float                     | 44.3 ms                                                                                                       | 49.7 ms: 1.12x slower                                                                                     |
| fannkuch                  | 215 ms                                                                                                        | 243 ms: 1.13x slower                                                                                      |
| scimark_fft               | 150 ms                                                                                                        | 171 ms: 1.14x slower                                                                                      |
| scimark_sparse_mat_mult   | 2.19 ms                                                                                                       | 2.50 ms: 1.14x slower                                                                                     |
| mako                      | 5.13 ms                                                                                                       | 6.36 ms: 1.24x slower                                                                                     |
| nbody                     | 53.1 ms                                                                                                       | 67.6 ms: 1.27x slower                                                                                     |
| spectral_norm             | 45.3 ms                                                                                                       | 63.7 ms: 1.41x slower                                                                                     |
| Geometric mean            | (ref)                                                                                                         | 1.04x faster                                                                                              |

Benchmark hidden because not significant (13): asyncio_tcp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, comprehensions, flaskblogging, pickle_pure_python, gc_traversal, pidigits, async_tree_io, pycparser, pickle_list, asyncio_tcp_ssl, regex_v8
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: sqlglot_normalize

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown