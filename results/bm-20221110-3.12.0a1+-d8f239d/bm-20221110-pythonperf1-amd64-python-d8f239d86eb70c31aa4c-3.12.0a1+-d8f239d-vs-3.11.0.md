
# Results vs. 3.11.0

- fork: python
- ref: d8f239d86eb70c31aa4c
- machine: windows-amd64
- commit hash: d8f239d
- commit date: 2022-11-10
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 204 ms                                                                   | 203 ms: 1.01x faster                                                        |
| chameleon      | 5.15 ms                                                                  | 5.01 ms: 1.03x faster                                                       |
| html5lib       | 38.5 ms                                                                  | 34.8 ms: 1.11x faster                                                       |
| tornado_http   | 91.8 ms                                                                  | 93.3 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                    | 1.03x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.9 ms                                                                  | 63.5 ms: 1.12x faster                                                       |
| pidigits       | 147 ms                                                                   | 153 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.02x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 89.7 ms                                                                  | 85.4 ms: 1.05x faster                                                       |
| regex_effbot   | 1.63 ms                                                                  | 1.57 ms: 1.04x faster                                                       |
| regex_v8       | 13.5 ms                                                                  | 13.6 ms: 1.01x slower                                                       |
| regex_dna      | 115 ms                                                                   | 121 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.71 ms                                                                  | 5.52 ms: 1.40x faster                                                       |
| unpickle_list        | 2.80 us                                                                  | 2.55 us: 1.10x faster                                                       |
| unpickle_pure_python | 150 us                                                                   | 138 us: 1.09x faster                                                        |
| pickle_pure_python   | 203 us                                                                   | 198 us: 1.03x faster                                                        |
| json_loads           | 13.5 us                                                                  | 13.2 us: 1.03x faster                                                       |
| xml_etree_generate   | 52.3 ms                                                                  | 51.6 ms: 1.01x faster                                                       |
| unpickle             | 8.01 us                                                                  | 8.22 us: 1.03x slower                                                       |
| pickle_dict          | 18.6 us                                                                  | 19.2 us: 1.03x slower                                                       |
| xml_etree_iterparse  | 61.8 ms                                                                  | 63.9 ms: 1.03x slower                                                       |
| pickle_list          | 2.70 us                                                                  | 2.88 us: 1.07x slower                                                       |
| pickle               | 6.47 us                                                                  | 7.20 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                                    | 1.02x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 18.4 ms                                                                  | 18.7 ms: 1.02x slower                                                       |
| python_startup_no_site | 15.4 ms                                                                  | 15.9 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                                    | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.20 ms                                                                  | 6.42 ms: 1.12x faster                                                       |
| django_template | 23.9 ms                                                                  | 22.0 ms: 1.08x faster                                                       |
| genshi_xml      | 38.0 ms                                                                  | 35.5 ms: 1.07x faster                                                       |
| genshi_text     | 17.3 ms                                                                  | 16.1 ms: 1.07x faster                                                       |
| Geometric mean  | (ref)                                                                    | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 7.71 ms                                                                  | 5.52 ms: 1.40x faster                                                       |
| mypy2                   | 276 ms                                                                   | 226 ms: 1.22x faster                                                        |
| unpack_sequence         | 43.1 ns                                                                  | 35.5 ns: 1.21x faster                                                       |
| richards                | 32.1 ms                                                                  | 27.6 ms: 1.16x faster                                                       |
| json                    | 3.20 ms                                                                  | 2.75 ms: 1.16x faster                                                       |
| mako                    | 7.20 ms                                                                  | 6.42 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.35 ms: 1.12x faster                                                       |
| nbody                   | 70.9 ms                                                                  | 63.5 ms: 1.12x faster                                                       |
| deltablue               | 2.68 ms                                                                  | 2.42 ms: 1.11x faster                                                       |
| html5lib                | 38.5 ms                                                                  | 34.8 ms: 1.11x faster                                                       |
| unpickle_list           | 2.80 us                                                                  | 2.55 us: 1.10x faster                                                       |
| spectral_norm           | 71.8 ms                                                                  | 65.8 ms: 1.09x faster                                                       |
| logging_silent          | 71.0 ns                                                                  | 65.3 ns: 1.09x faster                                                       |
| unpickle_pure_python    | 150 us                                                                   | 138 us: 1.09x faster                                                        |
| django_template         | 23.9 ms                                                                  | 22.0 ms: 1.08x faster                                                       |
| deepcopy_memo           | 25.3 us                                                                  | 23.4 us: 1.08x faster                                                       |
| fannkuch                | 255 ms                                                                   | 236 ms: 1.08x faster                                                        |
| nqueens                 | 65.1 ms                                                                  | 60.4 ms: 1.08x faster                                                       |
| raytrace                | 206 ms                                                                   | 191 ms: 1.08x faster                                                        |
| scimark_monte_carlo     | 45.8 ms                                                                  | 42.5 ms: 1.08x faster                                                       |
| sqlglot_optimize        | 34.5 ms                                                                  | 32.2 ms: 1.07x faster                                                       |
| genshi_xml              | 38.0 ms                                                                  | 35.5 ms: 1.07x faster                                                       |
| genshi_text             | 17.3 ms                                                                  | 16.1 ms: 1.07x faster                                                       |
| scimark_fft             | 183 ms                                                                   | 171 ms: 1.07x faster                                                        |
| go                      | 97.5 ms                                                                  | 92.1 ms: 1.06x faster                                                       |
| deepcopy_reduce         | 2.06 us                                                                  | 1.95 us: 1.06x faster                                                       |
| pprint_safe_repr        | 512 ms                                                                   | 485 ms: 1.06x faster                                                        |
| meteor_contest          | 74.4 ms                                                                  | 70.7 ms: 1.05x faster                                                       |
| crypto_pyaes            | 48.3 ms                                                                  | 45.9 ms: 1.05x faster                                                       |
| mdp                     | 1.67 sec                                                                 | 1.59 sec: 1.05x faster                                                      |
| regex_compile           | 89.7 ms                                                                  | 85.4 ms: 1.05x faster                                                       |
| pyflate                 | 302 ms                                                                   | 289 ms: 1.05x faster                                                        |
| pprint_pformat          | 1.05 sec                                                                 | 1.00 sec: 1.04x faster                                                      |
| sqlglot_transpile       | 1.13 ms                                                                  | 1.09 ms: 1.04x faster                                                       |
| regex_effbot            | 1.63 ms                                                                  | 1.57 ms: 1.04x faster                                                       |
| logging_format          | 7.13 us                                                                  | 6.85 us: 1.04x faster                                                       |
| sqlglot_normalize       | 189 ms                                                                   | 182 ms: 1.04x faster                                                        |
| hexiom                  | 4.46 ms                                                                  | 4.30 ms: 1.04x faster                                                       |
| pycparser               | 686 ms                                                                   | 662 ms: 1.04x faster                                                        |
| telco                   | 3.93 ms                                                                  | 3.79 ms: 1.04x faster                                                       |
| scimark_sor             | 77.7 ms                                                                  | 75.1 ms: 1.03x faster                                                       |
| deepcopy                | 240 us                                                                   | 232 us: 1.03x faster                                                        |
| chameleon               | 5.15 ms                                                                  | 5.01 ms: 1.03x faster                                                       |
| chaos                   | 47.3 ms                                                                  | 45.9 ms: 1.03x faster                                                       |
| sympy_expand            | 298 ms                                                                   | 290 ms: 1.03x faster                                                        |
| pickle_pure_python      | 203 us                                                                   | 198 us: 1.03x faster                                                        |
| json_loads              | 13.5 us                                                                  | 13.2 us: 1.03x faster                                                       |
| sqlglot_parse           | 929 us                                                                   | 907 us: 1.02x faster                                                        |
| async_generators        | 180 ms                                                                   | 176 ms: 1.02x faster                                                        |
| sympy_integrate         | 13.7 ms                                                                  | 13.4 ms: 1.02x faster                                                       |
| scimark_lu              | 62.8 ms                                                                  | 61.5 ms: 1.02x faster                                                       |
| coroutines              | 14.8 ms                                                                  | 14.5 ms: 1.02x faster                                                       |
| dask                    | 267 ms                                                                   | 261 ms: 1.02x faster                                                        |
| sympy_str               | 184 ms                                                                   | 180 ms: 1.02x faster                                                        |
| logging_simple          | 6.60 us                                                                  | 6.49 us: 1.02x faster                                                       |
| xml_etree_generate      | 52.3 ms                                                                  | 51.6 ms: 1.01x faster                                                       |
| dulwich_log             | 43.4 ms                                                                  | 43.1 ms: 1.01x faster                                                       |
| coverage                | 55.3 ms                                                                  | 54.9 ms: 1.01x faster                                                       |
| 2to3                    | 204 ms                                                                   | 203 ms: 1.01x faster                                                        |
| regex_v8                | 13.5 ms                                                                  | 13.6 ms: 1.01x slower                                                       |
| tornado_http            | 91.8 ms                                                                  | 93.3 ms: 1.02x slower                                                       |
| pathlib                 | 72.9 ms                                                                  | 74.2 ms: 1.02x slower                                                       |
| python_startup          | 18.4 ms                                                                  | 18.7 ms: 1.02x slower                                                       |
| generators              | 33.5 ms                                                                  | 34.4 ms: 1.02x slower                                                       |
| unpickle                | 8.01 us                                                                  | 8.22 us: 1.03x slower                                                       |
| pickle_dict             | 18.6 us                                                                  | 19.2 us: 1.03x slower                                                       |
| comprehensions          | 15.4 us                                                                  | 15.9 us: 1.03x slower                                                       |
| python_startup_no_site  | 15.4 ms                                                                  | 15.9 ms: 1.03x slower                                                       |
| xml_etree_iterparse     | 61.8 ms                                                                  | 63.9 ms: 1.03x slower                                                       |
| thrift                  | 487 us                                                                   | 505 us: 1.04x slower                                                        |
| bench_mp_pool           | 61.2 ms                                                                  | 63.5 ms: 1.04x slower                                                       |
| create_gc_cycles        | 666 us                                                                   | 691 us: 1.04x slower                                                        |
| pidigits                | 147 ms                                                                   | 153 ms: 1.04x slower                                                        |
| regex_dna               | 115 ms                                                                   | 121 ms: 1.05x slower                                                        |
| async_tree_none         | 313 ms                                                                   | 330 ms: 1.05x slower                                                        |
| async_tree_memoization  | 374 ms                                                                   | 394 ms: 1.05x slower                                                        |
| async_tree_io           | 744 ms                                                                   | 788 ms: 1.06x slower                                                        |
| gc_traversal            | 1.40 ms                                                                  | 1.49 ms: 1.06x slower                                                       |
| pickle_list             | 2.70 us                                                                  | 2.88 us: 1.07x slower                                                       |
| sqlite_synth            | 1.67 us                                                                  | 1.80 us: 1.08x slower                                                       |
| asyncio_tcp             | 674 ms                                                                   | 745 ms: 1.11x slower                                                        |
| pickle                  | 6.47 us                                                                  | 7.20 us: 1.11x slower                                                       |
| Geometric mean          | (ref)                                                                    | 1.03x faster                                                                |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, docutils, xml_etree_parse, float, xml_etree_process, sympy_sum, bench_thread_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
