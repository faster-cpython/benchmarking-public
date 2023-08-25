
# Results vs. 3.10.4

- fork: python
- ref: 4ae1a0ecaffe4320fe97
- machine: windows-amd64
- commit hash: 4ae1a0e
- commit date: 2022-10-25
- overall geometric mean: 1.13x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf1-amd64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 202 ms: 1.17x faster                                                       |
| chameleon      | 5.92 ms                                                     | 4.99 ms: 1.19x faster                                                      |
| docutils       | 1.89 sec                                                    | 1.59 sec: 1.19x faster                                                     |
| html5lib       | 46.5 ms                                                     | 38.1 ms: 1.22x faster                                                      |
| tornado_http   | 109 ms                                                      | 91.5 ms: 1.19x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf1-amd64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 53.5 ms: 1.13x faster                                                      |
| nbody          | 69.3 ms                                                     | 67.2 ms: 1.03x faster                                                      |
| pidigits       | 145 ms                                                      | 148 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf1-amd64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 86.3 ms: 1.20x faster                                                      |
| regex_dna      | 132 ms                                                      | 119 ms: 1.11x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 13.7 ms: 1.10x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf1-amd64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.62 ms: 1.51x faster                                                      |
| pickle_pure_python   | 257 us                                                      | 196 us: 1.31x faster                                                       |
| unpickle_pure_python | 171 us                                                      | 143 us: 1.20x faster                                                       |
| xml_etree_process    | 43.4 ms                                                     | 36.3 ms: 1.20x faster                                                      |
| xml_etree_parse      | 102 ms                                                      | 86.8 ms: 1.17x faster                                                      |
| unpickle_list        | 2.81 us                                                     | 2.60 us: 1.08x faster                                                      |
| xml_etree_generate   | 54.5 ms                                                     | 50.5 ms: 1.08x faster                                                      |
| json_loads           | 14.2 us                                                     | 13.5 us: 1.05x faster                                                      |
| pickle               | 6.80 us                                                     | 6.55 us: 1.04x faster                                                      |
| unpickle             | 9.17 us                                                     | 8.87 us: 1.03x faster                                                      |
| pickle_list          | 2.59 us                                                     | 2.64 us: 1.02x slower                                                      |
| pickle_dict          | 16.9 us                                                     | 18.2 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf1-amd64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                      |
| python_startup_no_site | 15.5 ms                                                     | 15.4 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf1-amd64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.93 ms: 1.27x faster                                                      |
| django_template | 28.2 ms                                                     | 23.8 ms: 1.19x faster                                                      |
| genshi_text     | 19.0 ms                                                     | 17.1 ms: 1.12x faster                                                      |
| genshi_xml      | 40.5 ms                                                     | 37.8 ms: 1.07x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf1-amd64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.51 ms: 1.66x faster                                                      |
| mypy2                   | 352 ms                                                      | 218 ms: 1.62x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.62 ms: 1.51x faster                                                      |
| go                      | 136 ms                                                      | 93.8 ms: 1.45x faster                                                      |
| scimark_sor             | 105 ms                                                      | 73.8 ms: 1.42x faster                                                      |
| logging_silent          | 96.4 ns                                                     | 68.8 ns: 1.40x faster                                                      |
| async_tree_io           | 1.07 sec                                                    | 775 ms: 1.37x faster                                                       |
| raytrace                | 271 ms                                                      | 204 ms: 1.33x faster                                                       |
| async_tree_none         | 420 ms                                                      | 316 ms: 1.33x faster                                                       |
| richards                | 41.2 ms                                                     | 31.0 ms: 1.33x faster                                                      |
| crypto_pyaes            | 62.3 ms                                                     | 47.2 ms: 1.32x faster                                                      |
| pickle_pure_python      | 257 us                                                      | 196 us: 1.31x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 381 ms: 1.31x faster                                                       |
| pyflate                 | 387 ms                                                      | 297 ms: 1.30x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.14 ms: 1.29x faster                                                      |
| scimark_lu              | 85.4 ms                                                     | 66.6 ms: 1.28x faster                                                      |
| sqlglot_parse           | 1.22 ms                                                     | 951 us: 1.28x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 43.8 ms: 1.28x faster                                                      |
| mako                    | 8.80 ms                                                     | 6.93 ms: 1.27x faster                                                      |
| chaos                   | 58.9 ms                                                     | 46.5 ms: 1.27x faster                                                      |
| thrift                  | 615 us                                                      | 486 us: 1.26x faster                                                       |
| async_generators        | 224 ms                                                      | 181 ms: 1.23x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 4.51 ms: 1.22x faster                                                      |
| html5lib                | 46.5 ms                                                     | 38.1 ms: 1.22x faster                                                      |
| pprint_pformat          | 1.21 sec                                                    | 1.00 sec: 1.21x faster                                                     |
| async_tree_cpu_io_mixed | 609 ms                                                      | 506 ms: 1.20x faster                                                       |
| pycparser               | 868 ms                                                      | 721 ms: 1.20x faster                                                       |
| regex_compile           | 103 ms                                                      | 86.3 ms: 1.20x faster                                                      |
| unpickle_pure_python    | 171 us                                                      | 143 us: 1.20x faster                                                       |
| xml_etree_process       | 43.4 ms                                                     | 36.3 ms: 1.20x faster                                                      |
| tornado_http            | 109 ms                                                      | 91.5 ms: 1.19x faster                                                      |
| pprint_safe_repr        | 589 ms                                                      | 495 ms: 1.19x faster                                                       |
| docutils                | 1.89 sec                                                    | 1.59 sec: 1.19x faster                                                     |
| chameleon               | 5.92 ms                                                     | 4.99 ms: 1.19x faster                                                      |
| django_template         | 28.2 ms                                                     | 23.8 ms: 1.19x faster                                                      |
| create_gc_cycles        | 782 us                                                      | 663 us: 1.18x faster                                                       |
| 2to3                    | 237 ms                                                      | 202 ms: 1.17x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 86.8 ms: 1.17x faster                                                      |
| deepcopy_memo           | 28.5 us                                                     | 24.7 us: 1.15x faster                                                      |
| dask                    | 305 ms                                                      | 265 ms: 1.15x faster                                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 34.4 ms: 1.13x faster                                                      |
| float                   | 60.2 ms                                                     | 53.5 ms: 1.13x faster                                                      |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.37 ms: 1.12x faster                                                      |
| bench_thread_pool       | 946 us                                                      | 844 us: 1.12x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 17.1 ms: 1.12x faster                                                      |
| sympy_integrate         | 14.8 ms                                                     | 13.4 ms: 1.11x faster                                                      |
| regex_dna               | 132 ms                                                      | 119 ms: 1.11x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 13.7 ms: 1.10x faster                                                      |
| json                    | 3.05 ms                                                     | 2.77 ms: 1.10x faster                                                      |
| python_startup          | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                      |
| dulwich_log             | 47.6 ms                                                     | 43.5 ms: 1.09x faster                                                      |
| pylint                  | 347 ms                                                      | 317 ms: 1.09x faster                                                       |
| deepcopy                | 255 us                                                      | 235 us: 1.09x faster                                                       |
| fannkuch                | 258 ms                                                      | 238 ms: 1.08x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.60 us: 1.08x faster                                                      |
| mdp                     | 1.71 sec                                                    | 1.59 sec: 1.08x faster                                                     |
| xml_etree_generate      | 54.5 ms                                                     | 50.5 ms: 1.08x faster                                                      |
| sqlglot_normalize       | 202 ms                                                      | 188 ms: 1.07x faster                                                       |
| genshi_xml              | 40.5 ms                                                     | 37.8 ms: 1.07x faster                                                      |
| sympy_expand            | 315 ms                                                      | 296 ms: 1.06x faster                                                       |
| coroutines              | 15.9 ms                                                     | 15.0 ms: 1.06x faster                                                      |
| spectral_norm           | 78.0 ms                                                     | 73.8 ms: 1.06x faster                                                      |
| sympy_sum               | 104 ms                                                      | 98.9 ms: 1.05x faster                                                      |
| deepcopy_reduce         | 2.16 us                                                     | 2.05 us: 1.05x faster                                                      |
| json_loads              | 14.2 us                                                     | 13.5 us: 1.05x faster                                                      |
| pathlib                 | 77.4 ms                                                     | 74.0 ms: 1.05x faster                                                      |
| pickle                  | 6.80 us                                                     | 6.55 us: 1.04x faster                                                      |
| unpickle                | 9.17 us                                                     | 8.87 us: 1.03x faster                                                      |
| nbody                   | 69.3 ms                                                     | 67.2 ms: 1.03x faster                                                      |
| scimark_fft             | 193 ms                                                      | 188 ms: 1.03x faster                                                       |
| sympy_str               | 188 ms                                                      | 183 ms: 1.03x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 65.4 ms: 1.02x faster                                                      |
| sqlite_synth            | 1.84 us                                                     | 1.80 us: 1.02x faster                                                      |
| comprehensions          | 16.0 us                                                     | 15.6 us: 1.02x faster                                                      |
| regex_effbot            | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| meteor_contest          | 72.5 ms                                                     | 71.8 ms: 1.01x faster                                                      |
| python_startup_no_site  | 15.5 ms                                                     | 15.4 ms: 1.01x faster                                                      |
| telco                   | 3.78 ms                                                     | 3.85 ms: 1.02x slower                                                      |
| pickle_list             | 2.59 us                                                     | 2.64 us: 1.02x slower                                                      |
| pidigits                | 145 ms                                                      | 148 ms: 1.02x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.42 ms: 1.06x slower                                                      |
| pickle_dict             | 16.9 us                                                     | 18.2 us: 1.08x slower                                                      |
| generators              | 31.6 ms                                                     | 34.5 ms: 1.09x slower                                                      |
| logging_format          | 6.66 us                                                     | 7.28 us: 1.09x slower                                                      |
| logging_simple          | 6.20 us                                                     | 6.80 us: 1.10x slower                                                      |
| unpack_sequence         | 37.8 ns                                                     | 42.3 ns: 1.12x slower                                                      |
| coverage                | 40.0 ms                                                     | 52.1 ms: 1.30x slower                                                      |
| Geometric mean          | (ref)                                                       | 1.13x faster                                                               |

Benchmark hidden because not significant (3): asyncio_tcp, xml_etree_iterparse, bench_mp_pool
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x
