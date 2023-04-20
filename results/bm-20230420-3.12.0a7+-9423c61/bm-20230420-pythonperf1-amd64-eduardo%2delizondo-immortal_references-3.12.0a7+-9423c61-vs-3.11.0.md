
# Results vs. 3.11.0

- fork: eduardo-elizondo
- ref: immortal_references
- machine: windows-amd64
- commit hash: 9423c61
- commit date: 2023-04-20
- overall geometric mean: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| chameleon      | 5.15 ms                                                                  | 4.88 ms: 1.06x faster                                                                  |
| docutils       | 1.59 sec                                                                 | 1.56 sec: 1.03x faster                                                                 |
| html5lib       | 38.5 ms                                                                  | 36.4 ms: 1.06x faster                                                                  |
| tornado_http   | 91.8 ms                                                                  | 88.8 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.03x faster                                                                           |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 53.3 ms                                                                  | 50.9 ms: 1.05x faster                                                                  |
| nbody          | 70.9 ms                                                                  | 68.3 ms: 1.04x faster                                                                  |
| pidigits       | 147 ms                                                                   | 148 ms: 1.01x slower                                                                   |
| Geometric mean | (ref)                                                                    | 1.02x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 89.7 ms                                                                  | 82.1 ms: 1.09x faster                                                                  |
| regex_effbot   | 1.63 ms                                                                  | 1.60 ms: 1.02x faster                                                                  |
| regex_v8       | 13.5 ms                                                                  | 14.1 ms: 1.05x slower                                                                  |
| regex_dna      | 115 ms                                                                   | 123 ms: 1.07x slower                                                                   |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 7.71 ms                                                                  | 5.36 ms: 1.44x faster                                                                  |
| unpickle_pure_python | 150 us                                                                   | 132 us: 1.13x faster                                                                   |
| pickle_pure_python   | 203 us                                                                   | 188 us: 1.08x faster                                                                   |
| xml_etree_parse      | 92.1 ms                                                                  | 88.1 ms: 1.05x faster                                                                  |
| json_loads           | 13.5 us                                                                  | 13.0 us: 1.04x faster                                                                  |
| unpickle_list        | 2.80 us                                                                  | 2.71 us: 1.03x faster                                                                  |
| xml_etree_iterparse  | 61.8 ms                                                                  | 60.0 ms: 1.03x faster                                                                  |
| pickle_dict          | 18.6 us                                                                  | 18.3 us: 1.02x faster                                                                  |
| xml_etree_process    | 36.6 ms                                                                  | 36.2 ms: 1.01x faster                                                                  |
| unpickle             | 8.01 us                                                                  | 8.18 us: 1.02x slower                                                                  |
| pickle_list          | 2.70 us                                                                  | 2.80 us: 1.04x slower                                                                  |
| pickle               | 6.47 us                                                                  | 6.82 us: 1.05x slower                                                                  |
| Geometric mean       | (ref)                                                                    | 1.05x faster                                                                           |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup | 18.4 ms                                                                  | 18.2 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|-----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_xml      | 38.0 ms                                                                  | 31.9 ms: 1.19x faster                                                                  |
| genshi_text     | 17.3 ms                                                                  | 14.9 ms: 1.16x faster                                                                  |
| django_template | 23.9 ms                                                                  | 21.7 ms: 1.10x faster                                                                  |
| mako            | 7.20 ms                                                                  | 6.62 ms: 1.09x faster                                                                  |
| Geometric mean  | (ref)                                                                    | 1.13x faster                                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|-------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| generators              | 33.5 ms                                                                  | 21.5 ms: 1.56x faster                                                                  |
| json_dumps              | 7.71 ms                                                                  | 5.36 ms: 1.44x faster                                                                  |
| asyncio_tcp             | 674 ms                                                                   | 475 ms: 1.42x faster                                                                   |
| mypy2                   | 276 ms                                                                   | 214 ms: 1.29x faster                                                                   |
| mdp                     | 1.67 sec                                                                 | 1.34 sec: 1.25x faster                                                                 |
| deltablue               | 2.68 ms                                                                  | 2.17 ms: 1.23x faster                                                                  |
| richards                | 32.1 ms                                                                  | 26.5 ms: 1.21x faster                                                                  |
| logging_silent          | 71.0 ns                                                                  | 58.9 ns: 1.21x faster                                                                  |
| genshi_xml              | 38.0 ms                                                                  | 31.9 ms: 1.19x faster                                                                  |
| spectral_norm           | 71.8 ms                                                                  | 60.5 ms: 1.19x faster                                                                  |
| sqlglot_parse           | 929 us                                                                   | 787 us: 1.18x faster                                                                   |
| json                    | 3.20 ms                                                                  | 2.74 ms: 1.17x faster                                                                  |
| pylint                  | 319 ms                                                                   | 274 ms: 1.16x faster                                                                   |
| genshi_text             | 17.3 ms                                                                  | 14.9 ms: 1.16x faster                                                                  |
| scimark_lu              | 62.8 ms                                                                  | 54.3 ms: 1.16x faster                                                                  |
| sqlglot_transpile       | 1.13 ms                                                                  | 988 us: 1.14x faster                                                                   |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.31 ms: 1.14x faster                                                                  |
| unpickle_pure_python    | 150 us                                                                   | 132 us: 1.13x faster                                                                   |
| go                      | 97.5 ms                                                                  | 86.2 ms: 1.13x faster                                                                  |
| raytrace                | 206 ms                                                                   | 182 ms: 1.13x faster                                                                   |
| nqueens                 | 65.1 ms                                                                  | 57.8 ms: 1.13x faster                                                                  |
| unpack_sequence         | 43.1 ns                                                                  | 38.4 ns: 1.12x faster                                                                  |
| hexiom                  | 4.46 ms                                                                  | 3.97 ms: 1.12x faster                                                                  |
| chaos                   | 47.3 ms                                                                  | 42.5 ms: 1.11x faster                                                                  |
| deepcopy_memo           | 25.3 us                                                                  | 22.9 us: 1.11x faster                                                                  |
| coroutines              | 14.8 ms                                                                  | 13.4 ms: 1.11x faster                                                                  |
| django_template         | 23.9 ms                                                                  | 21.7 ms: 1.10x faster                                                                  |
| regex_compile           | 89.7 ms                                                                  | 82.1 ms: 1.09x faster                                                                  |
| coverage                | 55.3 ms                                                                  | 50.6 ms: 1.09x faster                                                                  |
| sympy_expand            | 298 ms                                                                   | 274 ms: 1.09x faster                                                                   |
| scimark_monte_carlo     | 45.8 ms                                                                  | 42.1 ms: 1.09x faster                                                                  |
| mako                    | 7.20 ms                                                                  | 6.62 ms: 1.09x faster                                                                  |
| async_tree_cpu_io_mixed | 512 ms                                                                   | 471 ms: 1.09x faster                                                                   |
| logging_format          | 7.13 us                                                                  | 6.58 us: 1.08x faster                                                                  |
| pickle_pure_python      | 203 us                                                                   | 188 us: 1.08x faster                                                                   |
| sympy_str               | 184 ms                                                                   | 171 ms: 1.08x faster                                                                   |
| sqlglot_normalize       | 189 ms                                                                   | 176 ms: 1.07x faster                                                                   |
| scimark_fft             | 183 ms                                                                   | 170 ms: 1.07x faster                                                                   |
| sqlglot_optimize        | 34.5 ms                                                                  | 32.2 ms: 1.07x faster                                                                  |
| async_tree_memoization  | 374 ms                                                                   | 350 ms: 1.07x faster                                                                   |
| logging_simple          | 6.60 us                                                                  | 6.20 us: 1.07x faster                                                                  |
| dulwich_log             | 43.4 ms                                                                  | 40.9 ms: 1.06x faster                                                                  |
| bench_thread_pool       | 856 us                                                                   | 809 us: 1.06x faster                                                                   |
| html5lib                | 38.5 ms                                                                  | 36.4 ms: 1.06x faster                                                                  |
| chameleon               | 5.15 ms                                                                  | 4.88 ms: 1.06x faster                                                                  |
| pprint_safe_repr        | 512 ms                                                                   | 484 ms: 1.06x faster                                                                   |
| crypto_pyaes            | 48.3 ms                                                                  | 45.9 ms: 1.05x faster                                                                  |
| pprint_pformat          | 1.05 sec                                                                 | 999 ms: 1.05x faster                                                                   |
| deepcopy_reduce         | 2.06 us                                                                  | 1.96 us: 1.05x faster                                                                  |
| deepcopy                | 240 us                                                                   | 228 us: 1.05x faster                                                                   |
| pyflate                 | 302 ms                                                                   | 288 ms: 1.05x faster                                                                   |
| float                   | 53.3 ms                                                                  | 50.9 ms: 1.05x faster                                                                  |
| xml_etree_parse         | 92.1 ms                                                                  | 88.1 ms: 1.05x faster                                                                  |
| sympy_sum               | 98.9 ms                                                                  | 94.7 ms: 1.04x faster                                                                  |
| json_loads              | 13.5 us                                                                  | 13.0 us: 1.04x faster                                                                  |
| sympy_integrate         | 13.7 ms                                                                  | 13.1 ms: 1.04x faster                                                                  |
| pycparser               | 686 ms                                                                   | 659 ms: 1.04x faster                                                                   |
| fannkuch                | 255 ms                                                                   | 245 ms: 1.04x faster                                                                   |
| comprehensions          | 15.4 us                                                                  | 14.8 us: 1.04x faster                                                                  |
| nbody                   | 70.9 ms                                                                  | 68.3 ms: 1.04x faster                                                                  |
| unpickle_list           | 2.80 us                                                                  | 2.71 us: 1.03x faster                                                                  |
| tornado_http            | 91.8 ms                                                                  | 88.8 ms: 1.03x faster                                                                  |
| async_tree_none         | 313 ms                                                                   | 304 ms: 1.03x faster                                                                   |
| xml_etree_iterparse     | 61.8 ms                                                                  | 60.0 ms: 1.03x faster                                                                  |
| telco                   | 3.93 ms                                                                  | 3.82 ms: 1.03x faster                                                                  |
| thrift                  | 487 us                                                                   | 473 us: 1.03x faster                                                                   |
| docutils                | 1.59 sec                                                                 | 1.56 sec: 1.03x faster                                                                 |
| regex_effbot            | 1.63 ms                                                                  | 1.60 ms: 1.02x faster                                                                  |
| pickle_dict             | 18.6 us                                                                  | 18.3 us: 1.02x faster                                                                  |
| xml_etree_process       | 36.6 ms                                                                  | 36.2 ms: 1.01x faster                                                                  |
| python_startup          | 18.4 ms                                                                  | 18.2 ms: 1.01x faster                                                                  |
| pidigits                | 147 ms                                                                   | 148 ms: 1.01x slower                                                                   |
| scimark_sor             | 77.7 ms                                                                  | 79.0 ms: 1.02x slower                                                                  |
| async_tree_io           | 744 ms                                                                   | 759 ms: 1.02x slower                                                                   |
| unpickle                | 8.01 us                                                                  | 8.18 us: 1.02x slower                                                                  |
| gc_traversal            | 1.40 ms                                                                  | 1.43 ms: 1.02x slower                                                                  |
| meteor_contest          | 74.4 ms                                                                  | 76.2 ms: 1.02x slower                                                                  |
| create_gc_cycles        | 666 us                                                                   | 686 us: 1.03x slower                                                                   |
| pickle_list             | 2.70 us                                                                  | 2.80 us: 1.04x slower                                                                  |
| regex_v8                | 13.5 ms                                                                  | 14.1 ms: 1.05x slower                                                                  |
| pickle                  | 6.47 us                                                                  | 6.82 us: 1.05x slower                                                                  |
| regex_dna               | 115 ms                                                                   | 123 ms: 1.07x slower                                                                   |
| sqlite_synth            | 1.67 us                                                                  | 1.79 us: 1.07x slower                                                                  |
| bench_mp_pool           | 61.2 ms                                                                  | 66.3 ms: 1.08x slower                                                                  |
| pathlib                 | 72.9 ms                                                                  | 81.2 ms: 1.11x slower                                                                  |
| async_generators        | 180 ms                                                                   | 217 ms: 1.20x slower                                                                   |
| dask                    | 267 ms                                                                   | 358 ms: 1.34x slower                                                                   |
| Geometric mean          | (ref)                                                                    | 1.07x faster                                                                           |

Benchmark hidden because not significant (3): 2to3, python_startup_no_site, xml_etree_generate
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
