
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: windows-amd64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 204 ms                                                                   | 208 ms: 1.02x slower                                                                   |
| tornado_http   | 91.8 ms                                                                  | 89.0 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 70.9 ms                                                                  | 68.6 ms: 1.03x faster                                                                  |
| float          | 53.3 ms                                                                  | 52.1 ms: 1.02x faster                                                                  |
| pidigits       | 147 ms                                                                   | 150 ms: 1.02x slower                                                                   |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 89.7 ms                                                                  | 85.1 ms: 1.05x faster                                                                  |
| regex_effbot   | 1.63 ms                                                                  | 1.58 ms: 1.04x faster                                                                  |
| regex_dna      | 115 ms                                                                   | 116 ms: 1.01x slower                                                                   |
| regex_v8       | 13.5 ms                                                                  | 14.1 ms: 1.04x slower                                                                  |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 7.71 ms                                                                  | 5.60 ms: 1.38x faster                                                                  |
| unpickle_pure_python | 150 us                                                                   | 136 us: 1.10x faster                                                                   |
| pickle_pure_python   | 203 us                                                                   | 191 us: 1.06x faster                                                                   |
| pickle_dict          | 18.6 us                                                                  | 18.1 us: 1.03x faster                                                                  |
| xml_etree_iterparse  | 61.8 ms                                                                  | 61.1 ms: 1.01x faster                                                                  |
| unpickle_list        | 2.80 us                                                                  | 2.82 us: 1.01x slower                                                                  |
| xml_etree_process    | 36.6 ms                                                                  | 37.2 ms: 1.02x slower                                                                  |
| pickle_list          | 2.70 us                                                                  | 2.76 us: 1.02x slower                                                                  |
| json_loads           | 13.5 us                                                                  | 14.1 us: 1.04x slower                                                                  |
| xml_etree_generate   | 52.3 ms                                                                  | 54.6 ms: 1.04x slower                                                                  |
| unpickle             | 8.01 us                                                                  | 8.46 us: 1.06x slower                                                                  |
| pickle               | 6.47 us                                                                  | 6.95 us: 1.07x slower                                                                  |
| Geometric mean       | (ref)                                                                    | 1.02x faster                                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 18.4 ms                                                                  | 18.8 ms: 1.02x slower                                                                  |
| python_startup_no_site | 15.4 ms                                                                  | 15.9 ms: 1.04x slower                                                                  |
| Geometric mean         | (ref)                                                                    | 1.03x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-----------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako      | 7.20 ms                                                                  | 6.60 ms: 1.09x faster                                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| generators              | 33.5 ms                                                                  | 20.7 ms: 1.62x faster                                                                  |
| asyncio_tcp             | 674 ms                                                                   | 456 ms: 1.48x faster                                                                   |
| json_dumps              | 7.71 ms                                                                  | 5.60 ms: 1.38x faster                                                                  |
| deltablue               | 2.68 ms                                                                  | 2.05 ms: 1.30x faster                                                                  |
| mypy2                   | 276 ms                                                                   | 214 ms: 1.29x faster                                                                   |
| richards                | 32.1 ms                                                                  | 25.7 ms: 1.25x faster                                                                  |
| logging_silent          | 71.0 ns                                                                  | 58.1 ns: 1.22x faster                                                                  |
| mdp                     | 1.67 sec                                                                 | 1.42 sec: 1.18x faster                                                                 |
| sqlglot_parse           | 929 us                                                                   | 791 us: 1.18x faster                                                                   |
| sqlglot_transpile       | 1.13 ms                                                                  | 999 us: 1.13x faster                                                                   |
| hexiom                  | 4.46 ms                                                                  | 3.99 ms: 1.12x faster                                                                  |
| spectral_norm           | 71.8 ms                                                                  | 64.3 ms: 1.12x faster                                                                  |
| raytrace                | 206 ms                                                                   | 185 ms: 1.11x faster                                                                   |
| go                      | 97.5 ms                                                                  | 87.9 ms: 1.11x faster                                                                  |
| scimark_lu              | 62.8 ms                                                                  | 56.8 ms: 1.11x faster                                                                  |
| async_tree_cpu_io_mixed | 512 ms                                                                   | 464 ms: 1.10x faster                                                                   |
| unpickle_pure_python    | 150 us                                                                   | 136 us: 1.10x faster                                                                   |
| async_tree_memoization  | 374 ms                                                                   | 341 ms: 1.10x faster                                                                   |
| mako                    | 7.20 ms                                                                  | 6.60 ms: 1.09x faster                                                                  |
| nqueens                 | 65.1 ms                                                                  | 59.9 ms: 1.09x faster                                                                  |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.42 ms: 1.09x faster                                                                  |
| json                    | 3.20 ms                                                                  | 2.96 ms: 1.08x faster                                                                  |
| async_tree_none         | 313 ms                                                                   | 289 ms: 1.08x faster                                                                   |
| pickle_pure_python      | 203 us                                                                   | 191 us: 1.06x faster                                                                   |
| deepcopy_memo           | 25.3 us                                                                  | 23.9 us: 1.06x faster                                                                  |
| coroutines              | 14.8 ms                                                                  | 14.0 ms: 1.06x faster                                                                  |
| scimark_monte_carlo     | 45.8 ms                                                                  | 43.3 ms: 1.06x faster                                                                  |
| coverage                | 55.3 ms                                                                  | 52.3 ms: 1.06x faster                                                                  |
| chaos                   | 47.3 ms                                                                  | 44.8 ms: 1.06x faster                                                                  |
| regex_compile           | 89.7 ms                                                                  | 85.1 ms: 1.05x faster                                                                  |
| scimark_fft             | 183 ms                                                                   | 174 ms: 1.05x faster                                                                   |
| fannkuch                | 255 ms                                                                   | 244 ms: 1.05x faster                                                                   |
| pyflate                 | 302 ms                                                                   | 289 ms: 1.05x faster                                                                   |
| regex_effbot            | 1.63 ms                                                                  | 1.58 ms: 1.04x faster                                                                  |
| nbody                   | 70.9 ms                                                                  | 68.6 ms: 1.03x faster                                                                  |
| tornado_http            | 91.8 ms                                                                  | 89.0 ms: 1.03x faster                                                                  |
| pickle_dict             | 18.6 us                                                                  | 18.1 us: 1.03x faster                                                                  |
| pycparser               | 686 ms                                                                   | 666 ms: 1.03x faster                                                                   |
| async_tree_io           | 744 ms                                                                   | 727 ms: 1.02x faster                                                                   |
| float                   | 53.3 ms                                                                  | 52.1 ms: 1.02x faster                                                                  |
| deepcopy                | 240 us                                                                   | 234 us: 1.02x faster                                                                   |
| unpack_sequence         | 43.1 ns                                                                  | 42.2 ns: 1.02x faster                                                                  |
| sqlglot_normalize       | 189 ms                                                                   | 185 ms: 1.02x faster                                                                   |
| crypto_pyaes            | 48.3 ms                                                                  | 47.4 ms: 1.02x faster                                                                  |
| logging_simple          | 6.60 us                                                                  | 6.51 us: 1.02x faster                                                                  |
| bench_thread_pool       | 856 us                                                                   | 843 us: 1.02x faster                                                                   |
| sqlglot_optimize        | 34.5 ms                                                                  | 34.0 ms: 1.01x faster                                                                  |
| pprint_pformat          | 1.05 sec                                                                 | 1.04 sec: 1.01x faster                                                                 |
| logging_format          | 7.13 us                                                                  | 7.03 us: 1.01x faster                                                                  |
| xml_etree_iterparse     | 61.8 ms                                                                  | 61.1 ms: 1.01x faster                                                                  |
| dulwich_log             | 43.4 ms                                                                  | 43.1 ms: 1.01x faster                                                                  |
| deepcopy_reduce         | 2.06 us                                                                  | 2.07 us: 1.01x slower                                                                  |
| scimark_sor             | 77.7 ms                                                                  | 78.1 ms: 1.01x slower                                                                  |
| unpickle_list           | 2.80 us                                                                  | 2.82 us: 1.01x slower                                                                  |
| regex_dna               | 115 ms                                                                   | 116 ms: 1.01x slower                                                                   |
| create_gc_cycles        | 666 us                                                                   | 676 us: 1.01x slower                                                                   |
| gc_traversal            | 1.40 ms                                                                  | 1.43 ms: 1.02x slower                                                                  |
| xml_etree_process       | 36.6 ms                                                                  | 37.2 ms: 1.02x slower                                                                  |
| 2to3                    | 204 ms                                                                   | 208 ms: 1.02x slower                                                                   |
| sqlite_synth            | 1.67 us                                                                  | 1.71 us: 1.02x slower                                                                  |
| python_startup          | 18.4 ms                                                                  | 18.8 ms: 1.02x slower                                                                  |
| pickle_list             | 2.70 us                                                                  | 2.76 us: 1.02x slower                                                                  |
| pidigits                | 147 ms                                                                   | 150 ms: 1.02x slower                                                                   |
| comprehensions          | 15.4 us                                                                  | 15.9 us: 1.03x slower                                                                  |
| python_startup_no_site  | 15.4 ms                                                                  | 15.9 ms: 1.04x slower                                                                  |
| regex_v8                | 13.5 ms                                                                  | 14.1 ms: 1.04x slower                                                                  |
| json_loads              | 13.5 us                                                                  | 14.1 us: 1.04x slower                                                                  |
| xml_etree_generate      | 52.3 ms                                                                  | 54.6 ms: 1.04x slower                                                                  |
| unpickle                | 8.01 us                                                                  | 8.46 us: 1.06x slower                                                                  |
| telco                   | 3.93 ms                                                                  | 4.14 ms: 1.06x slower                                                                  |
| meteor_contest          | 74.4 ms                                                                  | 79.0 ms: 1.06x slower                                                                  |
| pickle                  | 6.47 us                                                                  | 6.95 us: 1.07x slower                                                                  |
| bench_mp_pool           | 61.2 ms                                                                  | 67.1 ms: 1.10x slower                                                                  |
| pathlib                 | 72.9 ms                                                                  | 81.7 ms: 1.12x slower                                                                  |
| async_generators        | 180 ms                                                                   | 228 ms: 1.27x slower                                                                   |
| dask                    | 267 ms                                                                   | 366 ms: 1.37x slower                                                                   |
| Geometric mean          | (ref)                                                                    | 1.04x faster                                                                           |

Benchmark hidden because not significant (3): xml_etree_parse, pprint_safe_repr, docutils
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
