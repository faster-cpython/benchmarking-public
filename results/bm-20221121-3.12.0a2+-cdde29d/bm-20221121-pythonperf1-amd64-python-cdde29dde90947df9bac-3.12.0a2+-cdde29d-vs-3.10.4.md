
# Results vs. 3.10.4

- fork: python
- ref: cdde29dde90947df9bac
- machine: windows-amd64
- commit hash: cdde29d
- commit date: 2022-11-21
- overall geometric mean: 1.20x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 194 ms: 1.22x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.62 ms: 1.28x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.55 sec: 1.22x faster                                                      |
| html5lib       | 46.5 ms                                                     | 34.8 ms: 1.33x faster                                                       |
| tornado_http   | 109 ms                                                      | 88.1 ms: 1.24x faster                                                       |
| Geometric mean | (ref)                                                       | 1.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 51.0 ms: 1.18x faster                                                       |
| nbody          | 69.3 ms                                                     | 59.0 ms: 1.18x faster                                                       |
| pidigits       | 145 ms                                                      | 148 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 81.1 ms: 1.27x faster                                                       |
| regex_dna      | 132 ms                                                      | 118 ms: 1.12x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 13.9 ms: 1.09x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.35 ms: 1.59x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 177 us: 1.45x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 131 us: 1.31x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 33.6 ms: 1.29x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 48.4 ms: 1.13x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 91.0 ms: 1.12x faster                                                       |
| json_loads           | 14.2 us                                                     | 12.9 us: 1.10x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.52 us: 1.08x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.64 us: 1.06x faster                                                       |
| pickle               | 6.80 us                                                     | 7.13 us: 1.05x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.73 us: 1.06x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 19.4 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.7 ms: 1.07x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.38 ms: 1.38x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 13.9 ms: 1.37x faster                                                       |
| django_template | 28.2 ms                                                     | 21.0 ms: 1.34x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 32.4 ms: 1.25x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.08 ms: 2.01x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 57.8 ns: 1.67x faster                                                       |
| richards                | 41.2 ms                                                     | 24.8 ms: 1.66x faster                                                       |
| go                      | 136 ms                                                      | 82.9 ms: 1.64x faster                                                       |
| mypy2                   | 352 ms                                                      | 216 ms: 1.63x faster                                                        |
| json_dumps              | 8.50 ms                                                     | 5.35 ms: 1.59x faster                                                       |
| scimark_sor             | 105 ms                                                      | 69.5 ms: 1.51x faster                                                       |
| raytrace                | 271 ms                                                      | 182 ms: 1.49x faster                                                        |
| sqlglot_parse           | 1.22 ms                                                     | 833 us: 1.46x faster                                                        |
| scimark_lu              | 85.4 ms                                                     | 58.9 ms: 1.45x faster                                                       |
| pyflate                 | 387 ms                                                      | 267 ms: 1.45x faster                                                        |
| pickle_pure_python      | 257 us                                                      | 177 us: 1.45x faster                                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 1.01 ms: 1.44x faster                                                       |
| unpack_sequence         | 37.8 ns                                                     | 26.3 ns: 1.44x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 3.87 ms: 1.43x faster                                                       |
| chaos                   | 58.9 ms                                                     | 42.2 ms: 1.40x faster                                                       |
| mako                    | 8.80 ms                                                     | 6.38 ms: 1.38x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 363 ms: 1.37x faster                                                        |
| genshi_text             | 19.0 ms                                                     | 13.9 ms: 1.37x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 45.7 ms: 1.36x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 783 ms: 1.36x faster                                                        |
| django_template         | 28.2 ms                                                     | 21.0 ms: 1.34x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 21.4 us: 1.34x faster                                                       |
| async_tree_none         | 420 ms                                                      | 314 ms: 1.34x faster                                                        |
| html5lib                | 46.5 ms                                                     | 34.8 ms: 1.33x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 42.3 ms: 1.32x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 131 us: 1.31x faster                                                        |
| spectral_norm           | 78.0 ms                                                     | 59.7 ms: 1.31x faster                                                       |
| xml_etree_process       | 43.4 ms                                                     | 33.6 ms: 1.29x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 934 ms: 1.29x faster                                                        |
| thrift                  | 615 us                                                      | 478 us: 1.29x faster                                                        |
| pprint_safe_repr        | 589 ms                                                      | 458 ms: 1.29x faster                                                        |
| chameleon               | 5.92 ms                                                     | 4.62 ms: 1.28x faster                                                       |
| regex_compile           | 103 ms                                                      | 81.1 ms: 1.27x faster                                                       |
| async_generators        | 224 ms                                                      | 176 ms: 1.27x faster                                                        |
| pycparser               | 868 ms                                                      | 691 ms: 1.26x faster                                                        |
| sqlglot_optimize        | 39.0 ms                                                     | 31.0 ms: 1.26x faster                                                       |
| genshi_xml              | 40.5 ms                                                     | 32.4 ms: 1.25x faster                                                       |
| tornado_http            | 109 ms                                                      | 88.1 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 496 ms: 1.23x faster                                                        |
| 2to3                    | 237 ms                                                      | 194 ms: 1.22x faster                                                        |
| docutils                | 1.89 sec                                                    | 1.55 sec: 1.22x faster                                                      |
| deepcopy                | 255 us                                                      | 212 us: 1.21x faster                                                        |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.24 ms: 1.19x faster                                                       |
| dask                    | 305 ms                                                      | 257 ms: 1.19x faster                                                        |
| deepcopy_reduce         | 2.16 us                                                     | 1.82 us: 1.18x faster                                                       |
| float                   | 60.2 ms                                                     | 51.0 ms: 1.18x faster                                                       |
| nbody                   | 69.3 ms                                                     | 59.0 ms: 1.18x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 57.1 ms: 1.17x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 174 ms: 1.16x faster                                                        |
| dulwich_log             | 47.6 ms                                                     | 41.1 ms: 1.16x faster                                                       |
| fannkuch                | 258 ms                                                      | 225 ms: 1.14x faster                                                        |
| sympy_expand            | 315 ms                                                      | 275 ms: 1.14x faster                                                        |
| create_gc_cycles        | 782 us                                                      | 685 us: 1.14x faster                                                        |
| sympy_integrate         | 14.8 ms                                                     | 13.0 ms: 1.14x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 48.4 ms: 1.13x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 842 us: 1.12x faster                                                        |
| xml_etree_parse         | 102 ms                                                      | 91.0 ms: 1.12x faster                                                       |
| regex_dna               | 132 ms                                                      | 118 ms: 1.12x faster                                                        |
| mdp                     | 1.71 sec                                                    | 1.54 sec: 1.11x faster                                                      |
| coroutines              | 15.9 ms                                                     | 14.5 ms: 1.10x faster                                                       |
| scimark_fft             | 193 ms                                                      | 175 ms: 1.10x faster                                                        |
| json                    | 3.05 ms                                                     | 2.78 ms: 1.10x faster                                                       |
| json_loads              | 14.2 us                                                     | 12.9 us: 1.10x faster                                                       |
| sympy_sum               | 104 ms                                                      | 95.2 ms: 1.09x faster                                                       |
| sympy_str               | 188 ms                                                      | 173 ms: 1.09x faster                                                        |
| regex_v8                | 15.0 ms                                                     | 13.9 ms: 1.09x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                       |
| unpickle                | 9.17 us                                                     | 8.52 us: 1.08x faster                                                       |
| python_startup          | 20.0 ms                                                     | 18.7 ms: 1.07x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.64 us: 1.06x faster                                                       |
| comprehensions          | 16.0 us                                                     | 15.1 us: 1.06x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 69.2 ms: 1.05x faster                                                       |
| logging_format          | 6.66 us                                                     | 6.39 us: 1.04x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.80 us: 1.02x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 76.4 ms: 1.01x faster                                                       |
| telco                   | 3.78 ms                                                     | 3.75 ms: 1.01x faster                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| pidigits                | 145 ms                                                      | 148 ms: 1.02x slower                                                        |
| bench_mp_pool           | 60.7 ms                                                     | 63.3 ms: 1.04x slower                                                       |
| pickle                  | 6.80 us                                                     | 7.13 us: 1.05x slower                                                       |
| asyncio_tcp             | 712 ms                                                      | 747 ms: 1.05x slower                                                        |
| pickle_list             | 2.59 us                                                     | 2.73 us: 1.06x slower                                                       |
| generators              | 31.6 ms                                                     | 34.4 ms: 1.09x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.48 ms: 1.10x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 19.4 us: 1.15x slower                                                       |
| coverage                | 40.0 ms                                                     | 53.2 ms: 1.33x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (2): logging_simple, xml_etree_iterparse
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x
