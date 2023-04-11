
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: windows-amd64
- commit hash: 2332a2e
- commit date: 2023-04-07
- overall geometric mean: 1.06x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 204 ms                                                                   | 209 ms: 1.03x slower                                                                   |
| chameleon      | 5.15 ms                                                                  | 4.71 ms: 1.10x faster                                                                  |
| html5lib       | 38.5 ms                                                                  | 37.4 ms: 1.03x faster                                                                  |
| tornado_http   | 91.8 ms                                                                  | 86.8 ms: 1.06x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.03x faster                                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 70.9 ms                                                                  | 62.0 ms: 1.14x faster                                                                  |
| float          | 53.3 ms                                                                  | 50.2 ms: 1.06x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.07x faster                                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 1.63 ms                                                                  | 1.54 ms: 1.06x faster                                                                  |
| regex_compile  | 89.7 ms                                                                  | 86.5 ms: 1.04x faster                                                                  |
| regex_dna      | 115 ms                                                                   | 120 ms: 1.04x slower                                                                   |
| regex_v8       | 13.5 ms                                                                  | 14.1 ms: 1.05x slower                                                                  |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 7.71 ms                                                                  | 5.51 ms: 1.40x faster                                                                  |
| unpickle_pure_python | 150 us                                                                   | 129 us: 1.16x faster                                                                   |
| pickle_pure_python   | 203 us                                                                   | 182 us: 1.12x faster                                                                   |
| json_loads           | 13.5 us                                                                  | 13.1 us: 1.03x faster                                                                  |
| xml_etree_process    | 36.6 ms                                                                  | 36.3 ms: 1.01x faster                                                                  |
| xml_etree_generate   | 52.3 ms                                                                  | 52.8 ms: 1.01x slower                                                                  |
| xml_etree_parse      | 92.1 ms                                                                  | 94.2 ms: 1.02x slower                                                                  |
| unpickle             | 8.01 us                                                                  | 8.43 us: 1.05x slower                                                                  |
| pickle_dict          | 18.6 us                                                                  | 19.6 us: 1.05x slower                                                                  |
| xml_etree_iterparse  | 61.8 ms                                                                  | 65.3 ms: 1.06x slower                                                                  |
| pickle_list          | 2.70 us                                                                  | 2.93 us: 1.08x slower                                                                  |
| pickle               | 6.47 us                                                                  | 7.39 us: 1.14x slower                                                                  |
| Geometric mean       | (ref)                                                                    | 1.02x faster                                                                           |

Benchmark hidden because not significant (1): unpickle_list

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
| genshi_xml      | 38.0 ms                                                                  | 31.1 ms: 1.22x faster                                                                  |
| genshi_text     | 17.3 ms                                                                  | 14.2 ms: 1.22x faster                                                                  |
| mako            | 7.20 ms                                                                  | 6.38 ms: 1.13x faster                                                                  |
| django_template | 23.9 ms                                                                  | 22.0 ms: 1.08x faster                                                                  |
| Geometric mean  | (ref)                                                                    | 1.16x faster                                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpack_sequence         | 43.1 ns                                                                  | 27.3 ns: 1.58x faster                                                                  |
| generators              | 33.5 ms                                                                  | 21.5 ms: 1.56x faster                                                                  |
| json_dumps              | 7.71 ms                                                                  | 5.51 ms: 1.40x faster                                                                  |
| asyncio_tcp             | 674 ms                                                                   | 489 ms: 1.38x faster                                                                   |
| deltablue               | 2.68 ms                                                                  | 2.01 ms: 1.33x faster                                                                  |
| logging_silent          | 71.0 ns                                                                  | 57.6 ns: 1.23x faster                                                                  |
| mypy2                   | 276 ms                                                                   | 225 ms: 1.23x faster                                                                   |
| sqlglot_parse           | 929 us                                                                   | 757 us: 1.23x faster                                                                   |
| genshi_xml              | 38.0 ms                                                                  | 31.1 ms: 1.22x faster                                                                  |
| genshi_text             | 17.3 ms                                                                  | 14.2 ms: 1.22x faster                                                                  |
| spectral_norm           | 71.8 ms                                                                  | 59.5 ms: 1.21x faster                                                                  |
| mdp                     | 1.67 sec                                                                 | 1.39 sec: 1.20x faster                                                                 |
| richards                | 32.1 ms                                                                  | 26.8 ms: 1.20x faster                                                                  |
| json                    | 3.20 ms                                                                  | 2.73 ms: 1.17x faster                                                                  |
| sqlglot_transpile       | 1.13 ms                                                                  | 974 us: 1.16x faster                                                                   |
| unpickle_pure_python    | 150 us                                                                   | 129 us: 1.16x faster                                                                   |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.28 ms: 1.15x faster                                                                  |
| nbody                   | 70.9 ms                                                                  | 62.0 ms: 1.14x faster                                                                  |
| deepcopy_memo           | 25.3 us                                                                  | 22.4 us: 1.13x faster                                                                  |
| scimark_lu              | 62.8 ms                                                                  | 55.6 ms: 1.13x faster                                                                  |
| go                      | 97.5 ms                                                                  | 86.3 ms: 1.13x faster                                                                  |
| mako                    | 7.20 ms                                                                  | 6.38 ms: 1.13x faster                                                                  |
| raytrace                | 206 ms                                                                   | 184 ms: 1.12x faster                                                                   |
| pickle_pure_python      | 203 us                                                                   | 182 us: 1.12x faster                                                                   |
| hexiom                  | 4.46 ms                                                                  | 4.06 ms: 1.10x faster                                                                  |
| chameleon               | 5.15 ms                                                                  | 4.71 ms: 1.10x faster                                                                  |
| scimark_monte_carlo     | 45.8 ms                                                                  | 41.9 ms: 1.09x faster                                                                  |
| nqueens                 | 65.1 ms                                                                  | 59.9 ms: 1.09x faster                                                                  |
| django_template         | 23.9 ms                                                                  | 22.0 ms: 1.08x faster                                                                  |
| scimark_fft             | 183 ms                                                                   | 169 ms: 1.08x faster                                                                   |
| pprint_pformat          | 1.05 sec                                                                 | 973 ms: 1.08x faster                                                                   |
| logging_format          | 7.13 us                                                                  | 6.63 us: 1.08x faster                                                                  |
| chaos                   | 47.3 ms                                                                  | 44.1 ms: 1.07x faster                                                                  |
| crypto_pyaes            | 48.3 ms                                                                  | 45.0 ms: 1.07x faster                                                                  |
| pprint_safe_repr        | 512 ms                                                                   | 479 ms: 1.07x faster                                                                   |
| async_tree_cpu_io_mixed | 512 ms                                                                   | 482 ms: 1.06x faster                                                                   |
| sqlglot_optimize        | 34.5 ms                                                                  | 32.5 ms: 1.06x faster                                                                  |
| sqlglot_normalize       | 189 ms                                                                   | 178 ms: 1.06x faster                                                                   |
| float                   | 53.3 ms                                                                  | 50.2 ms: 1.06x faster                                                                  |
| regex_effbot            | 1.63 ms                                                                  | 1.54 ms: 1.06x faster                                                                  |
| tornado_http            | 91.8 ms                                                                  | 86.8 ms: 1.06x faster                                                                  |
| logging_simple          | 6.60 us                                                                  | 6.25 us: 1.06x faster                                                                  |
| sympy_expand            | 298 ms                                                                   | 283 ms: 1.05x faster                                                                   |
| coverage                | 55.3 ms                                                                  | 52.7 ms: 1.05x faster                                                                  |
| deepcopy                | 240 us                                                                   | 229 us: 1.05x faster                                                                   |
| regex_compile           | 89.7 ms                                                                  | 86.5 ms: 1.04x faster                                                                  |
| pyflate                 | 302 ms                                                                   | 291 ms: 1.04x faster                                                                   |
| sympy_str               | 184 ms                                                                   | 178 ms: 1.03x faster                                                                   |
| json_loads              | 13.5 us                                                                  | 13.1 us: 1.03x faster                                                                  |
| html5lib                | 38.5 ms                                                                  | 37.4 ms: 1.03x faster                                                                  |
| async_tree_memoization  | 374 ms                                                                   | 365 ms: 1.02x faster                                                                   |
| pycparser               | 686 ms                                                                   | 670 ms: 1.02x faster                                                                   |
| fannkuch                | 255 ms                                                                   | 250 ms: 1.02x faster                                                                   |
| comprehensions          | 15.4 us                                                                  | 15.1 us: 1.02x faster                                                                  |
| deepcopy_reduce         | 2.06 us                                                                  | 2.02 us: 1.02x faster                                                                  |
| scimark_sor             | 77.7 ms                                                                  | 76.6 ms: 1.01x faster                                                                  |
| telco                   | 3.93 ms                                                                  | 3.88 ms: 1.01x faster                                                                  |
| sympy_integrate         | 13.7 ms                                                                  | 13.6 ms: 1.01x faster                                                                  |
| xml_etree_process       | 36.6 ms                                                                  | 36.3 ms: 1.01x faster                                                                  |
| xml_etree_generate      | 52.3 ms                                                                  | 52.8 ms: 1.01x slower                                                                  |
| async_tree_none         | 313 ms                                                                   | 317 ms: 1.01x slower                                                                   |
| sympy_sum               | 98.9 ms                                                                  | 101 ms: 1.02x slower                                                                   |
| xml_etree_parse         | 92.1 ms                                                                  | 94.2 ms: 1.02x slower                                                                  |
| 2to3                    | 204 ms                                                                   | 209 ms: 1.03x slower                                                                   |
| python_startup          | 18.4 ms                                                                  | 19.0 ms: 1.03x slower                                                                  |
| sqlite_synth            | 1.67 us                                                                  | 1.73 us: 1.04x slower                                                                  |
| create_gc_cycles        | 666 us                                                                   | 692 us: 1.04x slower                                                                   |
| regex_dna               | 115 ms                                                                   | 120 ms: 1.04x slower                                                                   |
| python_startup_no_site  | 15.4 ms                                                                  | 16.0 ms: 1.04x slower                                                                  |
| coroutines              | 14.8 ms                                                                  | 15.4 ms: 1.04x slower                                                                  |
| async_tree_io           | 744 ms                                                                   | 778 ms: 1.05x slower                                                                   |
| regex_v8                | 13.5 ms                                                                  | 14.1 ms: 1.05x slower                                                                  |
| unpickle                | 8.01 us                                                                  | 8.43 us: 1.05x slower                                                                  |
| pickle_dict             | 18.6 us                                                                  | 19.6 us: 1.05x slower                                                                  |
| xml_etree_iterparse     | 61.8 ms                                                                  | 65.3 ms: 1.06x slower                                                                  |
| gc_traversal            | 1.40 ms                                                                  | 1.49 ms: 1.06x slower                                                                  |
| pickle_list             | 2.70 us                                                                  | 2.93 us: 1.08x slower                                                                  |
| bench_mp_pool           | 61.2 ms                                                                  | 67.6 ms: 1.10x slower                                                                  |
| pickle                  | 6.47 us                                                                  | 7.39 us: 1.14x slower                                                                  |
| pathlib                 | 72.9 ms                                                                  | 88.8 ms: 1.22x slower                                                                  |
| async_generators        | 180 ms                                                                   | 221 ms: 1.23x slower                                                                   |
| dask                    | 267 ms                                                                   | 364 ms: 1.36x slower                                                                   |
| Geometric mean          | (ref)                                                                    | 1.06x faster                                                                           |

Benchmark hidden because not significant (7): pidigits, meteor_contest, thrift, dulwich_log, docutils, unpickle_list, bench_thread_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
