
# Results vs. 3.11.0

- fork: python
- ref: 3d5d3f7af6498effbc60
- machine: windows-amd64
- commit hash: 3d5d3f7
- commit date: 2023-01-10
- overall geometric mean: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 204 ms                                                                   | 193 ms: 1.06x faster                                                       |
| chameleon      | 5.15 ms                                                                  | 4.39 ms: 1.17x faster                                                      |
| docutils       | 1.59 sec                                                                 | 1.48 sec: 1.08x faster                                                     |
| html5lib       | 38.5 ms                                                                  | 33.7 ms: 1.14x faster                                                      |
| Geometric mean | (ref)                                                                    | 1.11x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 70.9 ms                                                                  | 59.5 ms: 1.19x faster                                                      |
| float          | 53.3 ms                                                                  | 47.2 ms: 1.13x faster                                                      |
| pidigits       | 147 ms                                                                   | 145 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.11x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 89.7 ms                                                                  | 78.8 ms: 1.14x faster                                                      |
| regex_effbot   | 1.63 ms                                                                  | 1.59 ms: 1.03x faster                                                      |
| regex_v8       | 13.5 ms                                                                  | 13.6 ms: 1.01x slower                                                      |
| regex_dna      | 115 ms                                                                   | 120 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                    | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.71 ms                                                                  | 5.10 ms: 1.51x faster                                                      |
| unpickle_pure_python | 150 us                                                                   | 119 us: 1.25x faster                                                       |
| pickle_pure_python   | 203 us                                                                   | 169 us: 1.20x faster                                                       |
| json_loads           | 13.5 us                                                                  | 12.4 us: 1.09x faster                                                      |
| unpickle_list        | 2.80 us                                                                  | 2.59 us: 1.08x faster                                                      |
| xml_etree_process    | 36.6 ms                                                                  | 33.8 ms: 1.08x faster                                                      |
| xml_etree_generate   | 52.3 ms                                                                  | 48.3 ms: 1.08x faster                                                      |
| xml_etree_parse      | 92.1 ms                                                                  | 86.5 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 61.8 ms                                                                  | 60.1 ms: 1.03x faster                                                      |
| pickle_dict          | 18.6 us                                                                  | 18.2 us: 1.02x faster                                                      |
| pickle               | 6.47 us                                                                  | 6.55 us: 1.01x slower                                                      |
| pickle_list          | 2.70 us                                                                  | 2.81 us: 1.04x slower                                                      |
| unpickle             | 8.01 us                                                                  | 8.70 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                                    | 1.09x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 18.4 ms                                                                  | 18.1 ms: 1.02x faster                                                      |
| python_startup_no_site | 15.4 ms                                                                  | 15.2 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                                    | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 17.3 ms                                                                  | 13.3 ms: 1.30x faster                                                      |
| genshi_xml      | 38.0 ms                                                                  | 30.5 ms: 1.25x faster                                                      |
| mako            | 7.20 ms                                                                  | 6.05 ms: 1.19x faster                                                      |
| django_template | 23.9 ms                                                                  | 20.7 ms: 1.15x faster                                                      |
| Geometric mean  | (ref)                                                                    | 1.22x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpack_sequence         | 43.1 ns                                                                  | 26.2 ns: 1.64x faster                                                      |
| json_dumps              | 7.71 ms                                                                  | 5.10 ms: 1.51x faster                                                      |
| asyncio_tcp             | 674 ms                                                                   | 466 ms: 1.44x faster                                                       |
| deltablue               | 2.68 ms                                                                  | 1.94 ms: 1.38x faster                                                      |
| richards                | 32.1 ms                                                                  | 24.0 ms: 1.34x faster                                                      |
| mypy2                   | 276 ms                                                                   | 209 ms: 1.32x faster                                                       |
| logging_silent          | 71.0 ns                                                                  | 54.2 ns: 1.31x faster                                                      |
| genshi_text             | 17.3 ms                                                                  | 13.3 ms: 1.30x faster                                                      |
| unpickle_pure_python    | 150 us                                                                   | 119 us: 1.25x faster                                                       |
| genshi_xml              | 38.0 ms                                                                  | 30.5 ms: 1.25x faster                                                      |
| deepcopy_memo           | 25.3 us                                                                  | 20.4 us: 1.24x faster                                                      |
| json                    | 3.20 ms                                                                  | 2.61 ms: 1.23x faster                                                      |
| scimark_sor             | 77.7 ms                                                                  | 63.7 ms: 1.22x faster                                                      |
| go                      | 97.5 ms                                                                  | 80.4 ms: 1.21x faster                                                      |
| scimark_monte_carlo     | 45.8 ms                                                                  | 38.0 ms: 1.20x faster                                                      |
| raytrace                | 206 ms                                                                   | 171 ms: 1.20x faster                                                       |
| pickle_pure_python      | 203 us                                                                   | 169 us: 1.20x faster                                                       |
| deepcopy                | 240 us                                                                   | 199 us: 1.20x faster                                                       |
| nbody                   | 70.9 ms                                                                  | 59.5 ms: 1.19x faster                                                      |
| mako                    | 7.20 ms                                                                  | 6.05 ms: 1.19x faster                                                      |
| hexiom                  | 4.46 ms                                                                  | 3.77 ms: 1.18x faster                                                      |
| fannkuch                | 255 ms                                                                   | 217 ms: 1.18x faster                                                       |
| chameleon               | 5.15 ms                                                                  | 4.39 ms: 1.17x faster                                                      |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.25 ms: 1.17x faster                                                      |
| deepcopy_reduce         | 2.06 us                                                                  | 1.78 us: 1.16x faster                                                      |
| django_template         | 23.9 ms                                                                  | 20.7 ms: 1.15x faster                                                      |
| pyflate                 | 302 ms                                                                   | 263 ms: 1.15x faster                                                       |
| pprint_pformat          | 1.05 sec                                                                 | 918 ms: 1.14x faster                                                       |
| spectral_norm           | 71.8 ms                                                                  | 62.8 ms: 1.14x faster                                                      |
| pprint_safe_repr        | 512 ms                                                                   | 448 ms: 1.14x faster                                                       |
| html5lib                | 38.5 ms                                                                  | 33.7 ms: 1.14x faster                                                      |
| regex_compile           | 89.7 ms                                                                  | 78.8 ms: 1.14x faster                                                      |
| nqueens                 | 65.1 ms                                                                  | 57.3 ms: 1.14x faster                                                      |
| logging_format          | 7.13 us                                                                  | 6.29 us: 1.13x faster                                                      |
| logging_simple          | 6.60 us                                                                  | 5.84 us: 1.13x faster                                                      |
| float                   | 53.3 ms                                                                  | 47.2 ms: 1.13x faster                                                      |
| sqlglot_optimize        | 34.5 ms                                                                  | 30.6 ms: 1.13x faster                                                      |
| chaos                   | 47.3 ms                                                                  | 42.1 ms: 1.12x faster                                                      |
| scimark_lu              | 62.8 ms                                                                  | 56.0 ms: 1.12x faster                                                      |
| sqlglot_normalize       | 189 ms                                                                   | 168 ms: 1.12x faster                                                       |
| sympy_expand            | 298 ms                                                                   | 269 ms: 1.11x faster                                                       |
| sqlglot_transpile       | 1.13 ms                                                                  | 1.02 ms: 1.11x faster                                                      |
| mdp                     | 1.67 sec                                                                 | 1.51 sec: 1.11x faster                                                     |
| async_tree_cpu_io_mixed | 512 ms                                                                   | 465 ms: 1.10x faster                                                       |
| scimark_fft             | 183 ms                                                                   | 167 ms: 1.10x faster                                                       |
| sqlglot_parse           | 929 us                                                                   | 848 us: 1.10x faster                                                       |
| async_tree_memoization  | 374 ms                                                                   | 342 ms: 1.10x faster                                                       |
| meteor_contest          | 74.4 ms                                                                  | 67.9 ms: 1.09x faster                                                      |
| sympy_str               | 184 ms                                                                   | 168 ms: 1.09x faster                                                       |
| telco                   | 3.93 ms                                                                  | 3.59 ms: 1.09x faster                                                      |
| pycparser               | 686 ms                                                                   | 628 ms: 1.09x faster                                                       |
| json_loads              | 13.5 us                                                                  | 12.4 us: 1.09x faster                                                      |
| dask                    | 267 ms                                                                   | 246 ms: 1.09x faster                                                       |
| sympy_integrate         | 13.7 ms                                                                  | 12.6 ms: 1.09x faster                                                      |
| dulwich_log             | 43.4 ms                                                                  | 40.1 ms: 1.08x faster                                                      |
| unpickle_list           | 2.80 us                                                                  | 2.59 us: 1.08x faster                                                      |
| xml_etree_process       | 36.6 ms                                                                  | 33.8 ms: 1.08x faster                                                      |
| xml_etree_generate      | 52.3 ms                                                                  | 48.3 ms: 1.08x faster                                                      |
| docutils                | 1.59 sec                                                                 | 1.48 sec: 1.08x faster                                                     |
| sympy_sum               | 98.9 ms                                                                  | 92.0 ms: 1.07x faster                                                      |
| bench_thread_pool       | 856 us                                                                   | 798 us: 1.07x faster                                                       |
| async_generators        | 180 ms                                                                   | 169 ms: 1.07x faster                                                       |
| coroutines              | 14.8 ms                                                                  | 13.9 ms: 1.06x faster                                                      |
| xml_etree_parse         | 92.1 ms                                                                  | 86.5 ms: 1.06x faster                                                      |
| async_tree_none         | 313 ms                                                                   | 295 ms: 1.06x faster                                                       |
| 2to3                    | 204 ms                                                                   | 193 ms: 1.06x faster                                                       |
| crypto_pyaes            | 48.3 ms                                                                  | 45.9 ms: 1.05x faster                                                      |
| coverage                | 55.3 ms                                                                  | 52.5 ms: 1.05x faster                                                      |
| thrift                  | 487 us                                                                   | 463 us: 1.05x faster                                                       |
| xml_etree_iterparse     | 61.8 ms                                                                  | 60.1 ms: 1.03x faster                                                      |
| regex_effbot            | 1.63 ms                                                                  | 1.59 ms: 1.03x faster                                                      |
| comprehensions          | 15.4 us                                                                  | 15.0 us: 1.02x faster                                                      |
| pickle_dict             | 18.6 us                                                                  | 18.2 us: 1.02x faster                                                      |
| python_startup          | 18.4 ms                                                                  | 18.1 ms: 1.02x faster                                                      |
| generators              | 33.5 ms                                                                  | 33.1 ms: 1.01x faster                                                      |
| python_startup_no_site  | 15.4 ms                                                                  | 15.2 ms: 1.01x faster                                                      |
| pidigits                | 147 ms                                                                   | 145 ms: 1.01x faster                                                       |
| create_gc_cycles        | 666 us                                                                   | 661 us: 1.01x faster                                                       |
| regex_v8                | 13.5 ms                                                                  | 13.6 ms: 1.01x slower                                                      |
| pickle                  | 6.47 us                                                                  | 6.55 us: 1.01x slower                                                      |
| gc_traversal            | 1.40 ms                                                                  | 1.43 ms: 1.02x slower                                                      |
| sqlite_synth            | 1.67 us                                                                  | 1.72 us: 1.03x slower                                                      |
| pickle_list             | 2.70 us                                                                  | 2.81 us: 1.04x slower                                                      |
| regex_dna               | 115 ms                                                                   | 120 ms: 1.04x slower                                                       |
| unpickle                | 8.01 us                                                                  | 8.70 us: 1.09x slower                                                      |
| Geometric mean          | (ref)                                                                    | 1.12x faster                                                               |

Benchmark hidden because not significant (3): async_tree_io, bench_mp_pool, pathlib
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
