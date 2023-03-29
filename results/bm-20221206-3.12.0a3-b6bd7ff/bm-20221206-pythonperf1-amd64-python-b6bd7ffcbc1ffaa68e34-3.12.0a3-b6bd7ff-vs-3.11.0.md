
# Results vs. 3.11.0

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: windows-amd64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.08x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 204 ms                                                                   | 196 ms: 1.04x faster                                                       |
| chameleon      | 5.15 ms                                                                  | 4.53 ms: 1.14x faster                                                      |
| docutils       | 1.59 sec                                                                 | 1.56 sec: 1.02x faster                                                     |
| html5lib       | 38.5 ms                                                                  | 35.0 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                                    | 1.07x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 70.9 ms                                                                  | 62.3 ms: 1.14x faster                                                      |
| float          | 53.3 ms                                                                  | 50.1 ms: 1.06x faster                                                      |
| pidigits       | 147 ms                                                                   | 151 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                    | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 89.7 ms                                                                  | 82.5 ms: 1.09x faster                                                      |
| regex_effbot   | 1.63 ms                                                                  | 1.54 ms: 1.06x faster                                                      |
| regex_v8       | 13.5 ms                                                                  | 14.0 ms: 1.04x slower                                                      |
| regex_dna      | 115 ms                                                                   | 120 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                    | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.71 ms                                                                  | 5.17 ms: 1.49x faster                                                      |
| unpickle_pure_python | 150 us                                                                   | 121 us: 1.24x faster                                                       |
| pickle_pure_python   | 203 us                                                                   | 179 us: 1.14x faster                                                       |
| unpickle_list        | 2.80 us                                                                  | 2.61 us: 1.07x faster                                                      |
| xml_etree_generate   | 52.3 ms                                                                  | 49.7 ms: 1.05x faster                                                      |
| json_loads           | 13.5 us                                                                  | 12.9 us: 1.05x faster                                                      |
| xml_etree_process    | 36.6 ms                                                                  | 35.0 ms: 1.05x faster                                                      |
| xml_etree_parse      | 92.1 ms                                                                  | 90.5 ms: 1.02x faster                                                      |
| pickle_dict          | 18.6 us                                                                  | 19.4 us: 1.04x slower                                                      |
| pickle_list          | 2.70 us                                                                  | 2.85 us: 1.05x slower                                                      |
| pickle               | 6.47 us                                                                  | 6.90 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                                    | 1.06x faster                                                               |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.4 ms                                                                  | 15.7 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 17.3 ms                                                                  | 13.8 ms: 1.25x faster                                                      |
| genshi_xml      | 38.0 ms                                                                  | 32.3 ms: 1.18x faster                                                      |
| mako            | 7.20 ms                                                                  | 6.19 ms: 1.16x faster                                                      |
| django_template | 23.9 ms                                                                  | 21.4 ms: 1.12x faster                                                      |
| Geometric mean  | (ref)                                                                    | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpack_sequence         | 43.1 ns                                                                  | 26.4 ns: 1.63x faster                                                      |
| json_dumps              | 7.71 ms                                                                  | 5.17 ms: 1.49x faster                                                      |
| richards                | 32.1 ms                                                                  | 24.5 ms: 1.31x faster                                                      |
| deltablue               | 2.68 ms                                                                  | 2.07 ms: 1.29x faster                                                      |
| mypy2                   | 276 ms                                                                   | 215 ms: 1.28x faster                                                       |
| genshi_text             | 17.3 ms                                                                  | 13.8 ms: 1.25x faster                                                      |
| logging_silent          | 71.0 ns                                                                  | 57.2 ns: 1.24x faster                                                      |
| unpickle_pure_python    | 150 us                                                                   | 121 us: 1.24x faster                                                       |
| scimark_monte_carlo     | 45.8 ms                                                                  | 38.1 ms: 1.20x faster                                                      |
| scimark_sor             | 77.7 ms                                                                  | 64.6 ms: 1.20x faster                                                      |
| deepcopy_memo           | 25.3 us                                                                  | 21.2 us: 1.20x faster                                                      |
| genshi_xml              | 38.0 ms                                                                  | 32.3 ms: 1.18x faster                                                      |
| json                    | 3.20 ms                                                                  | 2.74 ms: 1.17x faster                                                      |
| spectral_norm           | 71.8 ms                                                                  | 61.4 ms: 1.17x faster                                                      |
| mako                    | 7.20 ms                                                                  | 6.19 ms: 1.16x faster                                                      |
| raytrace                | 206 ms                                                                   | 179 ms: 1.15x faster                                                       |
| fannkuch                | 255 ms                                                                   | 222 ms: 1.15x faster                                                       |
| go                      | 97.5 ms                                                                  | 84.8 ms: 1.15x faster                                                      |
| hexiom                  | 4.46 ms                                                                  | 3.89 ms: 1.15x faster                                                      |
| pyflate                 | 302 ms                                                                   | 264 ms: 1.15x faster                                                       |
| scimark_lu              | 62.8 ms                                                                  | 54.8 ms: 1.15x faster                                                      |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.30 ms: 1.14x faster                                                      |
| chameleon               | 5.15 ms                                                                  | 4.53 ms: 1.14x faster                                                      |
| pickle_pure_python      | 203 us                                                                   | 179 us: 1.14x faster                                                       |
| nbody                   | 70.9 ms                                                                  | 62.3 ms: 1.14x faster                                                      |
| nqueens                 | 65.1 ms                                                                  | 57.9 ms: 1.12x faster                                                      |
| deepcopy                | 240 us                                                                   | 214 us: 1.12x faster                                                       |
| pprint_safe_repr        | 512 ms                                                                   | 458 ms: 1.12x faster                                                       |
| django_template         | 23.9 ms                                                                  | 21.4 ms: 1.12x faster                                                      |
| pprint_pformat          | 1.05 sec                                                                 | 947 ms: 1.11x faster                                                       |
| html5lib                | 38.5 ms                                                                  | 35.0 ms: 1.10x faster                                                      |
| sqlglot_normalize       | 189 ms                                                                   | 172 ms: 1.10x faster                                                       |
| deepcopy_reduce         | 2.06 us                                                                  | 1.88 us: 1.10x faster                                                      |
| chaos                   | 47.3 ms                                                                  | 43.2 ms: 1.10x faster                                                      |
| regex_compile           | 89.7 ms                                                                  | 82.5 ms: 1.09x faster                                                      |
| meteor_contest          | 74.4 ms                                                                  | 68.8 ms: 1.08x faster                                                      |
| sqlglot_parse           | 929 us                                                                   | 860 us: 1.08x faster                                                       |
| telco                   | 3.93 ms                                                                  | 3.64 ms: 1.08x faster                                                      |
| sqlglot_optimize        | 34.5 ms                                                                  | 32.0 ms: 1.08x faster                                                      |
| logging_format          | 7.13 us                                                                  | 6.64 us: 1.07x faster                                                      |
| unpickle_list           | 2.80 us                                                                  | 2.61 us: 1.07x faster                                                      |
| crypto_pyaes            | 48.3 ms                                                                  | 45.1 ms: 1.07x faster                                                      |
| coverage                | 55.3 ms                                                                  | 51.6 ms: 1.07x faster                                                      |
| sqlglot_transpile       | 1.13 ms                                                                  | 1.06 ms: 1.07x faster                                                      |
| sympy_str               | 184 ms                                                                   | 173 ms: 1.06x faster                                                       |
| float                   | 53.3 ms                                                                  | 50.1 ms: 1.06x faster                                                      |
| logging_simple          | 6.60 us                                                                  | 6.22 us: 1.06x faster                                                      |
| regex_effbot            | 1.63 ms                                                                  | 1.54 ms: 1.06x faster                                                      |
| dulwich_log             | 43.4 ms                                                                  | 41.2 ms: 1.06x faster                                                      |
| xml_etree_generate      | 52.3 ms                                                                  | 49.7 ms: 1.05x faster                                                      |
| json_loads              | 13.5 us                                                                  | 12.9 us: 1.05x faster                                                      |
| xml_etree_process       | 36.6 ms                                                                  | 35.0 ms: 1.05x faster                                                      |
| sympy_expand            | 298 ms                                                                   | 286 ms: 1.04x faster                                                       |
| mdp                     | 1.67 sec                                                                 | 1.61 sec: 1.04x faster                                                     |
| 2to3                    | 204 ms                                                                   | 196 ms: 1.04x faster                                                       |
| thrift                  | 487 us                                                                   | 469 us: 1.04x faster                                                       |
| dask                    | 267 ms                                                                   | 258 ms: 1.04x faster                                                       |
| scimark_fft             | 183 ms                                                                   | 177 ms: 1.03x faster                                                       |
| sympy_integrate         | 13.7 ms                                                                  | 13.3 ms: 1.03x faster                                                      |
| bench_thread_pool       | 856 us                                                                   | 837 us: 1.02x faster                                                       |
| async_tree_cpu_io_mixed | 512 ms                                                                   | 501 ms: 1.02x faster                                                       |
| docutils                | 1.59 sec                                                                 | 1.56 sec: 1.02x faster                                                     |
| xml_etree_parse         | 92.1 ms                                                                  | 90.5 ms: 1.02x faster                                                      |
| pathlib                 | 72.9 ms                                                                  | 72.1 ms: 1.01x faster                                                      |
| async_generators        | 180 ms                                                                   | 179 ms: 1.01x faster                                                       |
| comprehensions          | 15.4 us                                                                  | 15.5 us: 1.01x slower                                                      |
| generators              | 33.5 ms                                                                  | 33.9 ms: 1.01x slower                                                      |
| async_tree_none         | 313 ms                                                                   | 317 ms: 1.01x slower                                                       |
| coroutines              | 14.8 ms                                                                  | 15.1 ms: 1.02x slower                                                      |
| python_startup_no_site  | 15.4 ms                                                                  | 15.7 ms: 1.02x slower                                                      |
| create_gc_cycles        | 666 us                                                                   | 682 us: 1.02x slower                                                       |
| bench_mp_pool           | 61.2 ms                                                                  | 62.8 ms: 1.03x slower                                                      |
| gc_traversal            | 1.40 ms                                                                  | 1.44 ms: 1.03x slower                                                      |
| pidigits                | 147 ms                                                                   | 151 ms: 1.03x slower                                                       |
| sqlite_synth            | 1.67 us                                                                  | 1.73 us: 1.03x slower                                                      |
| regex_v8                | 13.5 ms                                                                  | 14.0 ms: 1.04x slower                                                      |
| async_tree_memoization  | 374 ms                                                                   | 388 ms: 1.04x slower                                                       |
| regex_dna               | 115 ms                                                                   | 120 ms: 1.04x slower                                                       |
| pickle_dict             | 18.6 us                                                                  | 19.4 us: 1.04x slower                                                      |
| async_tree_io           | 744 ms                                                                   | 780 ms: 1.05x slower                                                       |
| pickle_list             | 2.70 us                                                                  | 2.85 us: 1.05x slower                                                      |
| pickle                  | 6.47 us                                                                  | 6.90 us: 1.07x slower                                                      |
| asyncio_tcp             | 674 ms                                                                   | 735 ms: 1.09x slower                                                       |
| Geometric mean          | (ref)                                                                    | 1.08x faster                                                               |

Benchmark hidden because not significant (5): unpickle, sympy_sum, python_startup, xml_etree_iterparse, pycparser
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
