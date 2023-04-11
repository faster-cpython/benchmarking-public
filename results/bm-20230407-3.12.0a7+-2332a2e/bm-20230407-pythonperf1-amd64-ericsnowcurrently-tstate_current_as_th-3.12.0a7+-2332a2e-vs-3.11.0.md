
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: windows-amd64
- commit hash: 2332a2e
- commit date: 2023-04-07
- overall geometric mean: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 204 ms                                                                   | 210 ms: 1.03x slower                                                                   |
| chameleon      | 5.15 ms                                                                  | 4.55 ms: 1.13x faster                                                                  |
| html5lib       | 38.5 ms                                                                  | 37.3 ms: 1.03x faster                                                                  |
| tornado_http   | 91.8 ms                                                                  | 90.5 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.03x faster                                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 70.9 ms                                                                  | 58.2 ms: 1.22x faster                                                                  |
| float          | 53.3 ms                                                                  | 48.8 ms: 1.09x faster                                                                  |
| pidigits       | 147 ms                                                                   | 151 ms: 1.03x slower                                                                   |
| Geometric mean | (ref)                                                                    | 1.09x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 89.7 ms                                                                  | 83.0 ms: 1.08x faster                                                                  |
| regex_v8       | 13.5 ms                                                                  | 14.1 ms: 1.05x slower                                                                  |
| regex_dna      | 115 ms                                                                   | 123 ms: 1.07x slower                                                                   |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 7.71 ms                                                                  | 5.61 ms: 1.37x faster                                                                  |
| unpickle_pure_python | 150 us                                                                   | 125 us: 1.19x faster                                                                   |
| pickle_pure_python   | 203 us                                                                   | 176 us: 1.15x faster                                                                   |
| json_loads           | 13.5 us                                                                  | 13.0 us: 1.04x faster                                                                  |
| xml_etree_iterparse  | 61.8 ms                                                                  | 61.2 ms: 1.01x faster                                                                  |
| pickle_dict          | 18.6 us                                                                  | 18.9 us: 1.01x slower                                                                  |
| unpickle_list        | 2.80 us                                                                  | 2.85 us: 1.02x slower                                                                  |
| pickle_list          | 2.70 us                                                                  | 2.83 us: 1.05x slower                                                                  |
| unpickle             | 8.01 us                                                                  | 8.44 us: 1.05x slower                                                                  |
| pickle               | 6.47 us                                                                  | 7.04 us: 1.09x slower                                                                  |
| Geometric mean       | (ref)                                                                    | 1.04x faster                                                                           |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 18.4 ms                                                                  | 19.0 ms: 1.03x slower                                                                  |
| python_startup_no_site | 15.4 ms                                                                  | 16.0 ms: 1.04x slower                                                                  |
| Geometric mean         | (ref)                                                                    | 1.04x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_text     | 17.3 ms                                                                  | 13.4 ms: 1.28x faster                                                                  |
| genshi_xml      | 38.0 ms                                                                  | 30.4 ms: 1.25x faster                                                                  |
| mako            | 7.20 ms                                                                  | 6.23 ms: 1.16x faster                                                                  |
| django_template | 23.9 ms                                                                  | 21.9 ms: 1.09x faster                                                                  |
| Geometric mean  | (ref)                                                                    | 1.19x faster                                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpack_sequence         | 43.1 ns                                                                  | 26.4 ns: 1.63x faster                                                                  |
| generators              | 33.5 ms                                                                  | 20.8 ms: 1.62x faster                                                                  |
| json_dumps              | 7.71 ms                                                                  | 5.61 ms: 1.37x faster                                                                  |
| asyncio_tcp             | 674 ms                                                                   | 492 ms: 1.37x faster                                                                   |
| deltablue               | 2.68 ms                                                                  | 2.00 ms: 1.34x faster                                                                  |
| richards                | 32.1 ms                                                                  | 24.5 ms: 1.31x faster                                                                  |
| genshi_text             | 17.3 ms                                                                  | 13.4 ms: 1.28x faster                                                                  |
| logging_silent          | 71.0 ns                                                                  | 55.8 ns: 1.27x faster                                                                  |
| genshi_xml              | 38.0 ms                                                                  | 30.4 ms: 1.25x faster                                                                  |
| spectral_norm           | 71.8 ms                                                                  | 57.9 ms: 1.24x faster                                                                  |
| deepcopy_memo           | 25.3 us                                                                  | 20.5 us: 1.23x faster                                                                  |
| mypy2                   | 276 ms                                                                   | 224 ms: 1.23x faster                                                                   |
| nbody                   | 70.9 ms                                                                  | 58.2 ms: 1.22x faster                                                                  |
| sqlglot_parse           | 929 us                                                                   | 763 us: 1.22x faster                                                                   |
| unpickle_pure_python    | 150 us                                                                   | 125 us: 1.19x faster                                                                   |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.21 ms: 1.19x faster                                                                  |
| sqlglot_transpile       | 1.13 ms                                                                  | 952 us: 1.19x faster                                                                   |
| scimark_lu              | 62.8 ms                                                                  | 53.4 ms: 1.18x faster                                                                  |
| hexiom                  | 4.46 ms                                                                  | 3.81 ms: 1.17x faster                                                                  |
| raytrace                | 206 ms                                                                   | 177 ms: 1.16x faster                                                                   |
| go                      | 97.5 ms                                                                  | 84.3 ms: 1.16x faster                                                                  |
| mako                    | 7.20 ms                                                                  | 6.23 ms: 1.16x faster                                                                  |
| pickle_pure_python      | 203 us                                                                   | 176 us: 1.15x faster                                                                   |
| scimark_fft             | 183 ms                                                                   | 159 ms: 1.15x faster                                                                   |
| mdp                     | 1.67 sec                                                                 | 1.46 sec: 1.15x faster                                                                 |
| json                    | 3.20 ms                                                                  | 2.80 ms: 1.14x faster                                                                  |
| chaos                   | 47.3 ms                                                                  | 41.5 ms: 1.14x faster                                                                  |
| chameleon               | 5.15 ms                                                                  | 4.55 ms: 1.13x faster                                                                  |
| scimark_sor             | 77.7 ms                                                                  | 69.8 ms: 1.11x faster                                                                  |
| pprint_pformat          | 1.05 sec                                                                 | 951 ms: 1.10x faster                                                                   |
| scimark_monte_carlo     | 45.8 ms                                                                  | 41.6 ms: 1.10x faster                                                                  |
| deepcopy                | 240 us                                                                   | 218 us: 1.10x faster                                                                   |
| nqueens                 | 65.1 ms                                                                  | 59.5 ms: 1.09x faster                                                                  |
| pprint_safe_repr        | 512 ms                                                                   | 468 ms: 1.09x faster                                                                   |
| sqlglot_normalize       | 189 ms                                                                   | 173 ms: 1.09x faster                                                                   |
| logging_format          | 7.13 us                                                                  | 6.53 us: 1.09x faster                                                                  |
| float                   | 53.3 ms                                                                  | 48.8 ms: 1.09x faster                                                                  |
| django_template         | 23.9 ms                                                                  | 21.9 ms: 1.09x faster                                                                  |
| pyflate                 | 302 ms                                                                   | 279 ms: 1.08x faster                                                                   |
| deepcopy_reduce         | 2.06 us                                                                  | 1.90 us: 1.08x faster                                                                  |
| regex_compile           | 89.7 ms                                                                  | 83.0 ms: 1.08x faster                                                                  |
| fannkuch                | 255 ms                                                                   | 239 ms: 1.07x faster                                                                   |
| sqlglot_optimize        | 34.5 ms                                                                  | 32.3 ms: 1.07x faster                                                                  |
| comprehensions          | 15.4 us                                                                  | 14.6 us: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed | 512 ms                                                                   | 488 ms: 1.05x faster                                                                   |
| telco                   | 3.93 ms                                                                  | 3.76 ms: 1.04x faster                                                                  |
| sympy_expand            | 298 ms                                                                   | 286 ms: 1.04x faster                                                                   |
| pycparser               | 686 ms                                                                   | 658 ms: 1.04x faster                                                                   |
| json_loads              | 13.5 us                                                                  | 13.0 us: 1.04x faster                                                                  |
| coverage                | 55.3 ms                                                                  | 53.2 ms: 1.04x faster                                                                  |
| async_tree_memoization  | 374 ms                                                                   | 360 ms: 1.04x faster                                                                   |
| logging_simple          | 6.60 us                                                                  | 6.39 us: 1.03x faster                                                                  |
| html5lib                | 38.5 ms                                                                  | 37.3 ms: 1.03x faster                                                                  |
| crypto_pyaes            | 48.3 ms                                                                  | 47.2 ms: 1.02x faster                                                                  |
| tornado_http            | 91.8 ms                                                                  | 90.5 ms: 1.02x faster                                                                  |
| meteor_contest          | 74.4 ms                                                                  | 73.4 ms: 1.01x faster                                                                  |
| dulwich_log             | 43.4 ms                                                                  | 43.0 ms: 1.01x faster                                                                  |
| thrift                  | 487 us                                                                   | 482 us: 1.01x faster                                                                   |
| xml_etree_iterparse     | 61.8 ms                                                                  | 61.2 ms: 1.01x faster                                                                  |
| sqlite_synth            | 1.67 us                                                                  | 1.66 us: 1.01x faster                                                                  |
| sympy_str               | 184 ms                                                                   | 183 ms: 1.01x faster                                                                   |
| pickle_dict             | 18.6 us                                                                  | 18.9 us: 1.01x slower                                                                  |
| unpickle_list           | 2.80 us                                                                  | 2.85 us: 1.02x slower                                                                  |
| pidigits                | 147 ms                                                                   | 151 ms: 1.03x slower                                                                   |
| 2to3                    | 204 ms                                                                   | 210 ms: 1.03x slower                                                                   |
| python_startup          | 18.4 ms                                                                  | 19.0 ms: 1.03x slower                                                                  |
| sympy_sum               | 98.9 ms                                                                  | 102 ms: 1.03x slower                                                                   |
| python_startup_no_site  | 15.4 ms                                                                  | 16.0 ms: 1.04x slower                                                                  |
| async_tree_io           | 744 ms                                                                   | 777 ms: 1.05x slower                                                                   |
| regex_v8                | 13.5 ms                                                                  | 14.1 ms: 1.05x slower                                                                  |
| pickle_list             | 2.70 us                                                                  | 2.83 us: 1.05x slower                                                                  |
| unpickle                | 8.01 us                                                                  | 8.44 us: 1.05x slower                                                                  |
| regex_dna               | 115 ms                                                                   | 123 ms: 1.07x slower                                                                   |
| gc_traversal            | 1.40 ms                                                                  | 1.51 ms: 1.08x slower                                                                  |
| create_gc_cycles        | 666 us                                                                   | 718 us: 1.08x slower                                                                   |
| pickle                  | 6.47 us                                                                  | 7.04 us: 1.09x slower                                                                  |
| bench_mp_pool           | 61.2 ms                                                                  | 67.7 ms: 1.11x slower                                                                  |
| pathlib                 | 72.9 ms                                                                  | 84.4 ms: 1.16x slower                                                                  |
| async_generators        | 180 ms                                                                   | 227 ms: 1.26x slower                                                                   |
| dask                    | 267 ms                                                                   | 359 ms: 1.34x slower                                                                   |
| Geometric mean          | (ref)                                                                    | 1.07x faster                                                                           |

Benchmark hidden because not significant (9): coroutines, xml_etree_parse, docutils, bench_thread_pool, async_tree_none, xml_etree_generate, regex_effbot, sympy_integrate, xml_etree_process
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
