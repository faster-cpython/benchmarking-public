
# Results vs. 3.10.4

- fork: python
- ref: d8f239d86eb70c31aa4c
- machine: windows-amd64
- commit hash: d8f239d
- commit date: 2022-11-10
- overall geometric mean: 1.14x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 203 ms: 1.13x faster                                                        |
| chameleon      | 5.77 ms                                                                  | 5.01 ms: 1.15x faster                                                       |
| docutils       | 1.83 sec                                                                 | 1.59 sec: 1.15x faster                                                      |
| html5lib       | 47.3 ms                                                                  | 34.8 ms: 1.36x faster                                                       |
| tornado_http   | 106 ms                                                                   | 93.3 ms: 1.14x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.19x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.5 ms                                                                  | 63.5 ms: 1.12x faster                                                       |
| float          | 59.5 ms                                                                  | 53.0 ms: 1.12x faster                                                       |
| pidigits       | 145 ms                                                                   | 153 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 85.4 ms: 1.21x faster                                                       |
| regex_v8       | 15.1 ms                                                                  | 13.6 ms: 1.11x faster                                                       |
| regex_dna      | 131 ms                                                                   | 121 ms: 1.08x faster                                                        |
| regex_effbot   | 1.64 ms                                                                  | 1.57 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.00 ms                                                                  | 5.52 ms: 1.63x faster                                                       |
| pickle_pure_python   | 264 us                                                                   | 198 us: 1.33x faster                                                        |
| unpickle_pure_python | 179 us                                                                   | 138 us: 1.30x faster                                                        |
| xml_etree_process    | 43.0 ms                                                                  | 36.6 ms: 1.18x faster                                                       |
| unpickle             | 8.88 us                                                                  | 8.22 us: 1.08x faster                                                       |
| json_loads           | 14.2 us                                                                  | 13.2 us: 1.08x faster                                                       |
| unpickle_list        | 2.71 us                                                                  | 2.55 us: 1.06x faster                                                       |
| xml_etree_generate   | 53.8 ms                                                                  | 51.6 ms: 1.04x faster                                                       |
| xml_etree_parse      | 95.6 ms                                                                  | 91.7 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 62.5 ms                                                                  | 63.9 ms: 1.02x slower                                                       |
| pickle               | 6.67 us                                                                  | 7.20 us: 1.08x slower                                                       |
| pickle_list          | 2.57 us                                                                  | 2.88 us: 1.12x slower                                                       |
| pickle_dict          | 16.7 us                                                                  | 19.2 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                                    | 1.09x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 18.7 ms: 1.03x faster                                                       |
| python_startup_no_site | 14.8 ms                                                                  | 15.9 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                                    | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.69 ms                                                                  | 6.42 ms: 1.35x faster                                                       |
| django_template | 29.2 ms                                                                  | 22.0 ms: 1.33x faster                                                       |
| genshi_text     | 18.5 ms                                                                  | 16.1 ms: 1.15x faster                                                       |
| genshi_xml      | 38.8 ms                                                                  | 35.5 ms: 1.09x faster                                                       |
| Geometric mean  | (ref)                                                                    | 1.23x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 2.42 ms: 1.72x faster                                                       |
| json_dumps              | 9.00 ms                                                                  | 5.52 ms: 1.63x faster                                                       |
| go                      | 143 ms                                                                   | 92.1 ms: 1.56x faster                                                       |
| mypy2                   | 337 ms                                                                   | 226 ms: 1.49x faster                                                        |
| richards                | 41.0 ms                                                                  | 27.6 ms: 1.49x faster                                                       |
| logging_silent          | 94.6 ns                                                                  | 65.3 ns: 1.45x faster                                                       |
| raytrace                | 267 ms                                                                   | 191 ms: 1.40x faster                                                        |
| scimark_sor             | 104 ms                                                                   | 75.1 ms: 1.38x faster                                                       |
| scimark_lu              | 83.9 ms                                                                  | 61.5 ms: 1.36x faster                                                       |
| html5lib                | 47.3 ms                                                                  | 34.8 ms: 1.36x faster                                                       |
| mako                    | 8.69 ms                                                                  | 6.42 ms: 1.35x faster                                                       |
| sqlglot_transpile       | 1.47 ms                                                                  | 1.09 ms: 1.35x faster                                                       |
| pyflate                 | 388 ms                                                                   | 289 ms: 1.34x faster                                                        |
| sqlglot_parse           | 1.22 ms                                                                  | 907 us: 1.34x faster                                                        |
| crypto_pyaes            | 61.4 ms                                                                  | 45.9 ms: 1.34x faster                                                       |
| pickle_pure_python      | 264 us                                                                   | 198 us: 1.33x faster                                                        |
| django_template         | 29.2 ms                                                                  | 22.0 ms: 1.33x faster                                                       |
| pycparser               | 873 ms                                                                   | 662 ms: 1.32x faster                                                        |
| scimark_monte_carlo     | 56.0 ms                                                                  | 42.5 ms: 1.32x faster                                                       |
| unpickle_pure_python    | 179 us                                                                   | 138 us: 1.30x faster                                                        |
| async_tree_io           | 1.02 sec                                                                 | 788 ms: 1.30x faster                                                        |
| chaos                   | 58.4 ms                                                                  | 45.9 ms: 1.27x faster                                                       |
| hexiom                  | 5.45 ms                                                                  | 4.30 ms: 1.27x faster                                                       |
| async_tree_none         | 414 ms                                                                   | 330 ms: 1.26x faster                                                        |
| thrift                  | 632 us                                                                   | 505 us: 1.25x faster                                                        |
| async_tree_memoization  | 485 ms                                                                   | 394 ms: 1.23x faster                                                        |
| pprint_safe_repr        | 593 ms                                                                   | 485 ms: 1.22x faster                                                        |
| pprint_pformat          | 1.23 sec                                                                 | 1.00 sec: 1.22x faster                                                      |
| async_generators        | 214 ms                                                                   | 176 ms: 1.22x faster                                                        |
| deepcopy_memo           | 28.4 us                                                                  | 23.4 us: 1.21x faster                                                       |
| regex_compile           | 103 ms                                                                   | 85.4 ms: 1.21x faster                                                       |
| sqlglot_optimize        | 38.7 ms                                                                  | 32.2 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 508 ms: 1.19x faster                                                        |
| dask                    | 310 ms                                                                   | 261 ms: 1.19x faster                                                        |
| xml_etree_process       | 43.0 ms                                                                  | 36.6 ms: 1.18x faster                                                       |
| json                    | 3.18 ms                                                                  | 2.75 ms: 1.16x faster                                                       |
| docutils                | 1.83 sec                                                                 | 1.59 sec: 1.15x faster                                                      |
| chameleon               | 5.77 ms                                                                  | 5.01 ms: 1.15x faster                                                       |
| genshi_text             | 18.5 ms                                                                  | 16.1 ms: 1.15x faster                                                       |
| tornado_http            | 106 ms                                                                   | 93.3 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.35 ms: 1.13x faster                                                       |
| 2to3                    | 229 ms                                                                   | 203 ms: 1.13x faster                                                        |
| spectral_norm           | 74.3 ms                                                                  | 65.8 ms: 1.13x faster                                                       |
| nbody                   | 71.5 ms                                                                  | 63.5 ms: 1.12x faster                                                       |
| float                   | 59.5 ms                                                                  | 53.0 ms: 1.12x faster                                                       |
| deepcopy_reduce         | 2.18 us                                                                  | 1.95 us: 1.12x faster                                                       |
| bench_thread_pool       | 953 us                                                                   | 858 us: 1.11x faster                                                        |
| unpack_sequence         | 39.4 ns                                                                  | 35.5 ns: 1.11x faster                                                       |
| regex_v8                | 15.1 ms                                                                  | 13.6 ms: 1.11x faster                                                       |
| create_gc_cycles        | 764 us                                                                   | 691 us: 1.11x faster                                                        |
| sqlglot_normalize       | 201 ms                                                                   | 182 ms: 1.11x faster                                                        |
| deepcopy                | 256 us                                                                   | 232 us: 1.10x faster                                                        |
| sympy_integrate         | 14.7 ms                                                                  | 13.4 ms: 1.10x faster                                                       |
| scimark_fft             | 187 ms                                                                   | 171 ms: 1.09x faster                                                        |
| genshi_xml              | 38.8 ms                                                                  | 35.5 ms: 1.09x faster                                                       |
| dulwich_log             | 47.0 ms                                                                  | 43.1 ms: 1.09x faster                                                       |
| regex_dna               | 131 ms                                                                   | 121 ms: 1.08x faster                                                        |
| unpickle                | 8.88 us                                                                  | 8.22 us: 1.08x faster                                                       |
| sympy_expand            | 313 ms                                                                   | 290 ms: 1.08x faster                                                        |
| coroutines              | 15.6 ms                                                                  | 14.5 ms: 1.08x faster                                                       |
| json_loads              | 14.2 us                                                                  | 13.2 us: 1.08x faster                                                       |
| nqueens                 | 64.8 ms                                                                  | 60.4 ms: 1.07x faster                                                       |
| fannkuch                | 252 ms                                                                   | 236 ms: 1.07x faster                                                        |
| unpickle_list           | 2.71 us                                                                  | 2.55 us: 1.06x faster                                                       |
| meteor_contest          | 74.3 ms                                                                  | 70.7 ms: 1.05x faster                                                       |
| regex_effbot            | 1.64 ms                                                                  | 1.57 ms: 1.05x faster                                                       |
| sympy_str               | 189 ms                                                                   | 180 ms: 1.05x faster                                                        |
| xml_etree_generate      | 53.8 ms                                                                  | 51.6 ms: 1.04x faster                                                       |
| xml_etree_parse         | 95.6 ms                                                                  | 91.7 ms: 1.04x faster                                                       |
| sympy_sum               | 102 ms                                                                   | 99.1 ms: 1.03x faster                                                       |
| python_startup          | 19.3 ms                                                                  | 18.7 ms: 1.03x faster                                                       |
| sqlite_synth            | 1.85 us                                                                  | 1.80 us: 1.02x faster                                                       |
| pathlib                 | 75.2 ms                                                                  | 74.2 ms: 1.01x faster                                                       |
| telco                   | 3.77 ms                                                                  | 3.79 ms: 1.01x slower                                                       |
| xml_etree_iterparse     | 62.5 ms                                                                  | 63.9 ms: 1.02x slower                                                       |
| logging_format          | 6.53 us                                                                  | 6.85 us: 1.05x slower                                                       |
| pidigits                | 145 ms                                                                   | 153 ms: 1.05x slower                                                        |
| logging_simple          | 6.12 us                                                                  | 6.49 us: 1.06x slower                                                       |
| python_startup_no_site  | 14.8 ms                                                                  | 15.9 ms: 1.07x slower                                                       |
| bench_mp_pool           | 59.2 ms                                                                  | 63.5 ms: 1.07x slower                                                       |
| pickle                  | 6.67 us                                                                  | 7.20 us: 1.08x slower                                                       |
| generators              | 31.4 ms                                                                  | 34.4 ms: 1.09x slower                                                       |
| gc_traversal            | 1.33 ms                                                                  | 1.49 ms: 1.12x slower                                                       |
| pickle_list             | 2.57 us                                                                  | 2.88 us: 1.12x slower                                                       |
| asyncio_tcp             | 664 ms                                                                   | 745 ms: 1.12x slower                                                        |
| pickle_dict             | 16.7 us                                                                  | 19.2 us: 1.15x slower                                                       |
| coverage                | 37.5 ms                                                                  | 54.9 ms: 1.47x slower                                                       |
| Geometric mean          | (ref)                                                                    | 1.14x faster                                                                |

Benchmark hidden because not significant (2): comprehensions, mdp
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
