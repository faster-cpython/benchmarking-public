
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
| 2to3           | 204 ms                                                                   | 210 ms: 1.03x slower                                                                   |
| chameleon      | 5.15 ms                                                                  | 4.66 ms: 1.11x faster                                                                  |
| html5lib       | 38.5 ms                                                                  | 37.7 ms: 1.02x faster                                                                  |
| tornado_http   | 91.8 ms                                                                  | 90.7 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.02x faster                                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 70.9 ms                                                                  | 59.1 ms: 1.20x faster                                                                  |
| float          | 53.3 ms                                                                  | 50.1 ms: 1.06x faster                                                                  |
| pidigits       | 147 ms                                                                   | 153 ms: 1.04x slower                                                                   |
| Geometric mean | (ref)                                                                    | 1.07x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 1.63 ms                                                                  | 1.55 ms: 1.05x faster                                                                  |
| regex_compile  | 89.7 ms                                                                  | 86.2 ms: 1.04x faster                                                                  |
| regex_v8       | 13.5 ms                                                                  | 13.7 ms: 1.01x slower                                                                  |
| regex_dna      | 115 ms                                                                   | 119 ms: 1.03x slower                                                                   |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 7.71 ms                                                                  | 5.41 ms: 1.43x faster                                                                  |
| unpickle_pure_python | 150 us                                                                   | 127 us: 1.18x faster                                                                   |
| pickle_pure_python   | 203 us                                                                   | 186 us: 1.10x faster                                                                   |
| json_loads           | 13.5 us                                                                  | 13.2 us: 1.03x faster                                                                  |
| xml_etree_parse      | 92.1 ms                                                                  | 91.0 ms: 1.01x faster                                                                  |
| xml_etree_process    | 36.6 ms                                                                  | 36.9 ms: 1.01x slower                                                                  |
| xml_etree_iterparse  | 61.8 ms                                                                  | 63.1 ms: 1.02x slower                                                                  |
| pickle_dict          | 18.6 us                                                                  | 19.1 us: 1.03x slower                                                                  |
| unpickle             | 8.01 us                                                                  | 8.24 us: 1.03x slower                                                                  |
| xml_etree_generate   | 52.3 ms                                                                  | 53.8 ms: 1.03x slower                                                                  |
| unpickle_list        | 2.80 us                                                                  | 2.90 us: 1.04x slower                                                                  |
| pickle               | 6.47 us                                                                  | 6.84 us: 1.06x slower                                                                  |
| pickle_list          | 2.70 us                                                                  | 2.93 us: 1.08x slower                                                                  |
| Geometric mean       | (ref)                                                                    | 1.03x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 18.4 ms                                                                  | 19.0 ms: 1.03x slower                                                                  |
| python_startup_no_site | 15.4 ms                                                                  | 16.1 ms: 1.05x slower                                                                  |
| Geometric mean         | (ref)                                                                    | 1.04x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_xml      | 38.0 ms                                                                  | 31.6 ms: 1.20x faster                                                                  |
| genshi_text     | 17.3 ms                                                                  | 14.4 ms: 1.20x faster                                                                  |
| mako            | 7.20 ms                                                                  | 6.37 ms: 1.13x faster                                                                  |
| django_template | 23.9 ms                                                                  | 22.3 ms: 1.07x faster                                                                  |
| Geometric mean  | (ref)                                                                    | 1.15x faster                                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| generators              | 33.5 ms                                                                  | 21.3 ms: 1.58x faster                                                                  |
| unpack_sequence         | 43.1 ns                                                                  | 27.8 ns: 1.55x faster                                                                  |
| json_dumps              | 7.71 ms                                                                  | 5.41 ms: 1.43x faster                                                                  |
| asyncio_tcp             | 674 ms                                                                   | 488 ms: 1.38x faster                                                                   |
| deltablue               | 2.68 ms                                                                  | 2.00 ms: 1.34x faster                                                                  |
| logging_silent          | 71.0 ns                                                                  | 56.8 ns: 1.25x faster                                                                  |
| richards                | 32.1 ms                                                                  | 26.1 ms: 1.23x faster                                                                  |
| mypy2                   | 276 ms                                                                   | 225 ms: 1.23x faster                                                                   |
| genshi_xml              | 38.0 ms                                                                  | 31.6 ms: 1.20x faster                                                                  |
| genshi_text             | 17.3 ms                                                                  | 14.4 ms: 1.20x faster                                                                  |
| nbody                   | 70.9 ms                                                                  | 59.1 ms: 1.20x faster                                                                  |
| scimark_lu              | 62.8 ms                                                                  | 52.9 ms: 1.19x faster                                                                  |
| sqlglot_parse           | 929 us                                                                   | 782 us: 1.19x faster                                                                   |
| json                    | 3.20 ms                                                                  | 2.71 ms: 1.18x faster                                                                  |
| spectral_norm           | 71.8 ms                                                                  | 60.8 ms: 1.18x faster                                                                  |
| unpickle_pure_python    | 150 us                                                                   | 127 us: 1.18x faster                                                                   |
| sqlglot_transpile       | 1.13 ms                                                                  | 976 us: 1.16x faster                                                                   |
| mdp                     | 1.67 sec                                                                 | 1.45 sec: 1.16x faster                                                                 |
| raytrace                | 206 ms                                                                   | 179 ms: 1.15x faster                                                                   |
| mako                    | 7.20 ms                                                                  | 6.37 ms: 1.13x faster                                                                  |
| hexiom                  | 4.46 ms                                                                  | 3.97 ms: 1.12x faster                                                                  |
| deepcopy_memo           | 25.3 us                                                                  | 22.6 us: 1.12x faster                                                                  |
| chaos                   | 47.3 ms                                                                  | 42.3 ms: 1.12x faster                                                                  |
| scimark_fft             | 183 ms                                                                   | 164 ms: 1.11x faster                                                                   |
| chameleon               | 5.15 ms                                                                  | 4.66 ms: 1.11x faster                                                                  |
| nqueens                 | 65.1 ms                                                                  | 59.1 ms: 1.10x faster                                                                  |
| go                      | 97.5 ms                                                                  | 88.5 ms: 1.10x faster                                                                  |
| pickle_pure_python      | 203 us                                                                   | 186 us: 1.10x faster                                                                   |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.40 ms: 1.10x faster                                                                  |
| scimark_monte_carlo     | 45.8 ms                                                                  | 41.8 ms: 1.10x faster                                                                  |
| sqlglot_optimize        | 34.5 ms                                                                  | 31.6 ms: 1.09x faster                                                                  |
| sqlglot_normalize       | 189 ms                                                                   | 175 ms: 1.08x faster                                                                   |
| django_template         | 23.9 ms                                                                  | 22.3 ms: 1.07x faster                                                                  |
| pprint_pformat          | 1.05 sec                                                                 | 984 ms: 1.07x faster                                                                   |
| crypto_pyaes            | 48.3 ms                                                                  | 45.4 ms: 1.06x faster                                                                  |
| float                   | 53.3 ms                                                                  | 50.1 ms: 1.06x faster                                                                  |
| coverage                | 55.3 ms                                                                  | 52.1 ms: 1.06x faster                                                                  |
| sympy_expand            | 298 ms                                                                   | 283 ms: 1.06x faster                                                                   |
| pprint_safe_repr        | 512 ms                                                                   | 485 ms: 1.06x faster                                                                   |
| regex_effbot            | 1.63 ms                                                                  | 1.55 ms: 1.05x faster                                                                  |
| pycparser               | 686 ms                                                                   | 651 ms: 1.05x faster                                                                   |
| pyflate                 | 302 ms                                                                   | 288 ms: 1.05x faster                                                                   |
| deepcopy                | 240 us                                                                   | 229 us: 1.05x faster                                                                   |
| logging_format          | 7.13 us                                                                  | 6.84 us: 1.04x faster                                                                  |
| regex_compile           | 89.7 ms                                                                  | 86.2 ms: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed | 512 ms                                                                   | 493 ms: 1.04x faster                                                                   |
| deepcopy_reduce         | 2.06 us                                                                  | 2.00 us: 1.03x faster                                                                  |
| sympy_str               | 184 ms                                                                   | 179 ms: 1.03x faster                                                                   |
| logging_simple          | 6.60 us                                                                  | 6.43 us: 1.03x faster                                                                  |
| json_loads              | 13.5 us                                                                  | 13.2 us: 1.03x faster                                                                  |
| comprehensions          | 15.4 us                                                                  | 15.0 us: 1.02x faster                                                                  |
| sympy_integrate         | 13.7 ms                                                                  | 13.4 ms: 1.02x faster                                                                  |
| html5lib                | 38.5 ms                                                                  | 37.7 ms: 1.02x faster                                                                  |
| fannkuch                | 255 ms                                                                   | 251 ms: 1.02x faster                                                                   |
| meteor_contest          | 74.4 ms                                                                  | 73.3 ms: 1.01x faster                                                                  |
| dulwich_log             | 43.4 ms                                                                  | 42.9 ms: 1.01x faster                                                                  |
| xml_etree_parse         | 92.1 ms                                                                  | 91.0 ms: 1.01x faster                                                                  |
| tornado_http            | 91.8 ms                                                                  | 90.7 ms: 1.01x faster                                                                  |
| coroutines              | 14.8 ms                                                                  | 14.7 ms: 1.01x faster                                                                  |
| telco                   | 3.93 ms                                                                  | 3.90 ms: 1.01x faster                                                                  |
| xml_etree_process       | 36.6 ms                                                                  | 36.9 ms: 1.01x slower                                                                  |
| regex_v8                | 13.5 ms                                                                  | 13.7 ms: 1.01x slower                                                                  |
| sympy_sum               | 98.9 ms                                                                  | 100 ms: 1.01x slower                                                                   |
| thrift                  | 487 us                                                                   | 494 us: 1.02x slower                                                                   |
| xml_etree_iterparse     | 61.8 ms                                                                  | 63.1 ms: 1.02x slower                                                                  |
| async_tree_io           | 744 ms                                                                   | 760 ms: 1.02x slower                                                                   |
| pickle_dict             | 18.6 us                                                                  | 19.1 us: 1.03x slower                                                                  |
| unpickle                | 8.01 us                                                                  | 8.24 us: 1.03x slower                                                                  |
| regex_dna               | 115 ms                                                                   | 119 ms: 1.03x slower                                                                   |
| xml_etree_generate      | 52.3 ms                                                                  | 53.8 ms: 1.03x slower                                                                  |
| 2to3                    | 204 ms                                                                   | 210 ms: 1.03x slower                                                                   |
| sqlite_synth            | 1.67 us                                                                  | 1.72 us: 1.03x slower                                                                  |
| python_startup          | 18.4 ms                                                                  | 19.0 ms: 1.03x slower                                                                  |
| unpickle_list           | 2.80 us                                                                  | 2.90 us: 1.04x slower                                                                  |
| pidigits                | 147 ms                                                                   | 153 ms: 1.04x slower                                                                   |
| create_gc_cycles        | 666 us                                                                   | 695 us: 1.04x slower                                                                   |
| python_startup_no_site  | 15.4 ms                                                                  | 16.1 ms: 1.05x slower                                                                  |
| pickle                  | 6.47 us                                                                  | 6.84 us: 1.06x slower                                                                  |
| gc_traversal            | 1.40 ms                                                                  | 1.48 ms: 1.06x slower                                                                  |
| pickle_list             | 2.70 us                                                                  | 2.93 us: 1.08x slower                                                                  |
| bench_mp_pool           | 61.2 ms                                                                  | 66.9 ms: 1.09x slower                                                                  |
| pathlib                 | 72.9 ms                                                                  | 86.1 ms: 1.18x slower                                                                  |
| async_generators        | 180 ms                                                                   | 214 ms: 1.19x slower                                                                   |
| dask                    | 267 ms                                                                   | 357 ms: 1.34x slower                                                                   |
| Geometric mean          | (ref)                                                                    | 1.06x faster                                                                           |

Benchmark hidden because not significant (5): async_tree_none, scimark_sor, bench_thread_pool, docutils, async_tree_memoization
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
