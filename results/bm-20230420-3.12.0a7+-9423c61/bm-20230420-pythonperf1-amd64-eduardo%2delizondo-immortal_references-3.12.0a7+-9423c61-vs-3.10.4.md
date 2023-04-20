
# Results vs. 3.10.4

- fork: eduardo-elizondo
- ref: immortal_references
- machine: windows-amd64
- commit hash: 9423c61
- commit date: 2023-04-20
- overall geometric mean: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 204 ms: 1.12x faster                                                                   |
| chameleon      | 5.77 ms                                                                  | 4.88 ms: 1.18x faster                                                                  |
| docutils       | 1.83 sec                                                                 | 1.56 sec: 1.18x faster                                                                 |
| html5lib       | 47.3 ms                                                                  | 36.4 ms: 1.30x faster                                                                  |
| tornado_http   | 106 ms                                                                   | 88.8 ms: 1.20x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.20x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 59.5 ms                                                                  | 50.9 ms: 1.17x faster                                                                  |
| nbody          | 71.5 ms                                                                  | 68.3 ms: 1.05x faster                                                                  |
| pidigits       | 145 ms                                                                   | 148 ms: 1.02x slower                                                                   |
| Geometric mean | (ref)                                                                    | 1.06x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 82.1 ms: 1.26x faster                                                                  |
| regex_v8       | 15.1 ms                                                                  | 14.1 ms: 1.07x faster                                                                  |
| regex_dna      | 131 ms                                                                   | 123 ms: 1.07x faster                                                                   |
| regex_effbot   | 1.64 ms                                                                  | 1.60 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.10x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 9.00 ms                                                                  | 5.36 ms: 1.68x faster                                                                  |
| pickle_pure_python   | 264 us                                                                   | 188 us: 1.40x faster                                                                   |
| unpickle_pure_python | 179 us                                                                   | 132 us: 1.36x faster                                                                   |
| xml_etree_process    | 43.0 ms                                                                  | 36.2 ms: 1.19x faster                                                                  |
| json_loads           | 14.2 us                                                                  | 13.0 us: 1.09x faster                                                                  |
| unpickle             | 8.88 us                                                                  | 8.18 us: 1.09x faster                                                                  |
| xml_etree_parse      | 95.6 ms                                                                  | 88.1 ms: 1.09x faster                                                                  |
| xml_etree_iterparse  | 62.5 ms                                                                  | 60.0 ms: 1.04x faster                                                                  |
| xml_etree_generate   | 53.8 ms                                                                  | 52.4 ms: 1.03x faster                                                                  |
| pickle               | 6.67 us                                                                  | 6.82 us: 1.02x slower                                                                  |
| pickle_list          | 2.57 us                                                                  | 2.80 us: 1.09x slower                                                                  |
| pickle_dict          | 16.7 us                                                                  | 18.3 us: 1.10x slower                                                                  |
| Geometric mean       | (ref)                                                                    | 1.12x faster                                                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 18.2 ms: 1.06x faster                                                                  |
| python_startup_no_site | 14.8 ms                                                                  | 15.4 ms: 1.04x slower                                                                  |
| Geometric mean         | (ref)                                                                    | 1.01x faster                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|-----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 29.2 ms                                                                  | 21.7 ms: 1.34x faster                                                                  |
| mako            | 8.69 ms                                                                  | 6.62 ms: 1.31x faster                                                                  |
| genshi_text     | 18.5 ms                                                                  | 14.9 ms: 1.24x faster                                                                  |
| genshi_xml      | 38.8 ms                                                                  | 31.9 ms: 1.22x faster                                                                  |
| Geometric mean  | (ref)                                                                    | 1.28x faster                                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|-------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 2.17 ms: 1.91x faster                                                                  |
| json_dumps              | 9.00 ms                                                                  | 5.36 ms: 1.68x faster                                                                  |
| go                      | 143 ms                                                                   | 86.2 ms: 1.66x faster                                                                  |
| logging_silent          | 94.6 ns                                                                  | 58.9 ns: 1.61x faster                                                                  |
| mypy2                   | 337 ms                                                                   | 214 ms: 1.57x faster                                                                   |
| richards                | 41.0 ms                                                                  | 26.5 ms: 1.55x faster                                                                  |
| sqlglot_parse           | 1.22 ms                                                                  | 787 us: 1.55x faster                                                                   |
| scimark_lu              | 83.9 ms                                                                  | 54.3 ms: 1.54x faster                                                                  |
| sqlglot_transpile       | 1.47 ms                                                                  | 988 us: 1.49x faster                                                                   |
| raytrace                | 267 ms                                                                   | 182 ms: 1.46x faster                                                                   |
| generators              | 31.4 ms                                                                  | 21.5 ms: 1.46x faster                                                                  |
| pickle_pure_python      | 264 us                                                                   | 188 us: 1.40x faster                                                                   |
| asyncio_tcp             | 664 ms                                                                   | 475 ms: 1.40x faster                                                                   |
| async_tree_memoization  | 485 ms                                                                   | 350 ms: 1.39x faster                                                                   |
| chaos                   | 58.4 ms                                                                  | 42.5 ms: 1.38x faster                                                                  |
| hexiom                  | 5.45 ms                                                                  | 3.97 ms: 1.37x faster                                                                  |
| async_tree_none         | 414 ms                                                                   | 304 ms: 1.36x faster                                                                   |
| unpickle_pure_python    | 179 us                                                                   | 132 us: 1.36x faster                                                                   |
| async_tree_io           | 1.02 sec                                                                 | 759 ms: 1.35x faster                                                                   |
| pyflate                 | 388 ms                                                                   | 288 ms: 1.35x faster                                                                   |
| django_template         | 29.2 ms                                                                  | 21.7 ms: 1.34x faster                                                                  |
| crypto_pyaes            | 61.4 ms                                                                  | 45.9 ms: 1.34x faster                                                                  |
| thrift                  | 632 us                                                                   | 473 us: 1.34x faster                                                                   |
| scimark_monte_carlo     | 56.0 ms                                                                  | 42.1 ms: 1.33x faster                                                                  |
| pycparser               | 873 ms                                                                   | 659 ms: 1.33x faster                                                                   |
| mako                    | 8.69 ms                                                                  | 6.62 ms: 1.31x faster                                                                  |
| scimark_sor             | 104 ms                                                                   | 79.0 ms: 1.31x faster                                                                  |
| html5lib                | 47.3 ms                                                                  | 36.4 ms: 1.30x faster                                                                  |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 471 ms: 1.28x faster                                                                   |
| regex_compile           | 103 ms                                                                   | 82.1 ms: 1.26x faster                                                                  |
| genshi_text             | 18.5 ms                                                                  | 14.9 ms: 1.24x faster                                                                  |
| deepcopy_memo           | 28.4 us                                                                  | 22.9 us: 1.24x faster                                                                  |
| pylint                  | 337 ms                                                                   | 274 ms: 1.23x faster                                                                   |
| pprint_pformat          | 1.23 sec                                                                 | 999 ms: 1.23x faster                                                                   |
| spectral_norm           | 74.3 ms                                                                  | 60.5 ms: 1.23x faster                                                                  |
| pprint_safe_repr        | 593 ms                                                                   | 484 ms: 1.23x faster                                                                   |
| genshi_xml              | 38.8 ms                                                                  | 31.9 ms: 1.22x faster                                                                  |
| sqlglot_optimize        | 38.7 ms                                                                  | 32.2 ms: 1.20x faster                                                                  |
| mdp                     | 1.60 sec                                                                 | 1.34 sec: 1.20x faster                                                                 |
| tornado_http            | 106 ms                                                                   | 88.8 ms: 1.20x faster                                                                  |
| xml_etree_process       | 43.0 ms                                                                  | 36.2 ms: 1.19x faster                                                                  |
| chameleon               | 5.77 ms                                                                  | 4.88 ms: 1.18x faster                                                                  |
| docutils                | 1.83 sec                                                                 | 1.56 sec: 1.18x faster                                                                 |
| bench_thread_pool       | 953 us                                                                   | 809 us: 1.18x faster                                                                   |
| float                   | 59.5 ms                                                                  | 50.9 ms: 1.17x faster                                                                  |
| coroutines              | 15.6 ms                                                                  | 13.4 ms: 1.17x faster                                                                  |
| json                    | 3.18 ms                                                                  | 2.74 ms: 1.16x faster                                                                  |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.31 ms: 1.16x faster                                                                  |
| dulwich_log             | 47.0 ms                                                                  | 40.9 ms: 1.15x faster                                                                  |
| sqlglot_normalize       | 201 ms                                                                   | 176 ms: 1.14x faster                                                                   |
| sympy_expand            | 313 ms                                                                   | 274 ms: 1.14x faster                                                                   |
| 2to3                    | 229 ms                                                                   | 204 ms: 1.12x faster                                                                   |
| nqueens                 | 64.8 ms                                                                  | 57.8 ms: 1.12x faster                                                                  |
| deepcopy                | 256 us                                                                   | 228 us: 1.12x faster                                                                   |
| sympy_integrate         | 14.7 ms                                                                  | 13.1 ms: 1.12x faster                                                                  |
| create_gc_cycles        | 764 us                                                                   | 686 us: 1.11x faster                                                                   |
| deepcopy_reduce         | 2.18 us                                                                  | 1.96 us: 1.11x faster                                                                  |
| sympy_str               | 189 ms                                                                   | 171 ms: 1.10x faster                                                                   |
| scimark_fft             | 187 ms                                                                   | 170 ms: 1.10x faster                                                                   |
| json_loads              | 14.2 us                                                                  | 13.0 us: 1.09x faster                                                                  |
| unpickle                | 8.88 us                                                                  | 8.18 us: 1.09x faster                                                                  |
| xml_etree_parse         | 95.6 ms                                                                  | 88.1 ms: 1.09x faster                                                                  |
| comprehensions          | 16.0 us                                                                  | 14.8 us: 1.08x faster                                                                  |
| sympy_sum               | 102 ms                                                                   | 94.7 ms: 1.08x faster                                                                  |
| regex_v8                | 15.1 ms                                                                  | 14.1 ms: 1.07x faster                                                                  |
| regex_dna               | 131 ms                                                                   | 123 ms: 1.07x faster                                                                   |
| python_startup          | 19.3 ms                                                                  | 18.2 ms: 1.06x faster                                                                  |
| nbody                   | 71.5 ms                                                                  | 68.3 ms: 1.05x faster                                                                  |
| xml_etree_iterparse     | 62.5 ms                                                                  | 60.0 ms: 1.04x faster                                                                  |
| sqlite_synth            | 1.85 us                                                                  | 1.79 us: 1.03x faster                                                                  |
| regex_effbot            | 1.64 ms                                                                  | 1.60 ms: 1.03x faster                                                                  |
| xml_etree_generate      | 53.8 ms                                                                  | 52.4 ms: 1.03x faster                                                                  |
| fannkuch                | 252 ms                                                                   | 245 ms: 1.03x faster                                                                   |
| unpack_sequence         | 39.4 ns                                                                  | 38.4 ns: 1.03x faster                                                                  |
| logging_format          | 6.53 us                                                                  | 6.58 us: 1.01x slower                                                                  |
| async_generators        | 214 ms                                                                   | 217 ms: 1.01x slower                                                                   |
| logging_simple          | 6.12 us                                                                  | 6.20 us: 1.01x slower                                                                  |
| telco                   | 3.77 ms                                                                  | 3.82 ms: 1.01x slower                                                                  |
| pidigits                | 145 ms                                                                   | 148 ms: 1.02x slower                                                                   |
| pickle                  | 6.67 us                                                                  | 6.82 us: 1.02x slower                                                                  |
| meteor_contest          | 74.3 ms                                                                  | 76.2 ms: 1.03x slower                                                                  |
| python_startup_no_site  | 14.8 ms                                                                  | 15.4 ms: 1.04x slower                                                                  |
| gc_traversal            | 1.33 ms                                                                  | 1.43 ms: 1.08x slower                                                                  |
| pathlib                 | 75.2 ms                                                                  | 81.2 ms: 1.08x slower                                                                  |
| pickle_list             | 2.57 us                                                                  | 2.80 us: 1.09x slower                                                                  |
| pickle_dict             | 16.7 us                                                                  | 18.3 us: 1.10x slower                                                                  |
| bench_mp_pool           | 59.2 ms                                                                  | 66.3 ms: 1.12x slower                                                                  |
| dask                    | 310 ms                                                                   | 358 ms: 1.15x slower                                                                   |
| coverage                | 37.5 ms                                                                  | 50.6 ms: 1.35x slower                                                                  |
| Geometric mean          | (ref)                                                                    | 1.18x faster                                                                           |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
