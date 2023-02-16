
# Results vs. 3.11.0

- fork: faster-cpython
- ref: specialized_send
- machine: linux-x86_64
- commit hash: 685d559
- commit date: 2023-02-10
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 246 ms: 1.06x faster                                                         |
| chameleon      | 6.38 ms                                                | 6.51 ms: 1.02x slower                                                        |
| docutils       | 2.60 sec                                               | 2.54 sec: 1.02x faster                                                       |
| html5lib       | 64.8 ms                                                | 61.3 ms: 1.06x faster                                                        |
| tornado_http   | 96.5 ms                                                | 95.1 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.9 ms: 1.04x faster                                                        |
| pidigits       | 197 ms                                                 | 197 ms: 1.00x slower                                                         |
| nbody          | 90.0 ms                                                | 93.0 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 131 ms: 1.04x faster                                                         |
| regex_effbot   | 3.46 ms                                                | 3.38 ms: 1.02x faster                                                        |
| regex_dna      | 203 ms                                                 | 211 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.46 ms: 1.31x faster                                                        |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                                         |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                        |
| pickle_pure_python   | 308 us                                                 | 283 us: 1.09x faster                                                         |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                         |
| pickle_dict          | 31.2 us                                                | 30.9 us: 1.01x faster                                                        |
| pickle_list          | 4.14 us                                                | 4.12 us: 1.01x faster                                                        |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                                        |
| unpickle             | 13.3 us                                                | 13.7 us: 1.03x slower                                                        |
| xml_etree_process    | 53.7 ms                                                | 55.9 ms: 1.04x slower                                                        |
| xml_etree_generate   | 75.9 ms                                                | 80.6 ms: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.96 ms: 1.04x slower                                                        |
| python_startup_no_site | 6.04 ms                                                | 6.49 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.1 ms: 1.07x faster                                                        |
| genshi_text     | 21.5 ms                                                | 20.8 ms: 1.04x faster                                                        |
| mako            | 9.83 ms                                                | 9.75 ms: 1.01x faster                                                        |
| django_template | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.1 ms: 2.36x faster                                                        |
| asyncio_tcp             | 883 ms                                                 | 495 ms: 1.79x faster                                                         |
| json_dumps              | 12.4 ms                                                | 9.46 ms: 1.31x faster                                                        |
| mypy2                   | 420 ms                                                 | 330 ms: 1.27x faster                                                         |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.87 ms: 1.18x faster                                                        |
| coroutines              | 26.2 ms                                                | 22.3 ms: 1.18x faster                                                        |
| deltablue               | 3.66 ms                                                | 3.19 ms: 1.15x faster                                                        |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                                         |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                        |
| pickle_pure_python      | 308 us                                                 | 283 us: 1.09x faster                                                         |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                         |
| sympy_str               | 291 ms                                                 | 270 ms: 1.08x faster                                                         |
| richards                | 46.1 ms                                                | 42.9 ms: 1.07x faster                                                        |
| pycparser               | 1.19 sec                                               | 1.11 sec: 1.07x faster                                                       |
| genshi_xml              | 51.4 ms                                                | 48.1 ms: 1.07x faster                                                        |
| logging_simple          | 6.02 us                                                | 5.67 us: 1.06x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                                        |
| scimark_sor             | 115 ms                                                 | 109 ms: 1.06x faster                                                         |
| html5lib                | 64.8 ms                                                | 61.3 ms: 1.06x faster                                                        |
| 2to3                    | 259 ms                                                 | 246 ms: 1.06x faster                                                         |
| json                    | 4.87 ms                                                | 4.61 ms: 1.06x faster                                                        |
| sympy_sum               | 166 ms                                                 | 158 ms: 1.05x faster                                                         |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                         |
| regex_compile           | 136 ms                                                 | 131 ms: 1.04x faster                                                         |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.04x faster                                                         |
| logging_silent          | 98.0 ns                                                | 94.0 ns: 1.04x faster                                                        |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                                         |
| sqlglot_optimize        | 52.7 ms                                                | 50.6 ms: 1.04x faster                                                        |
| float                   | 76.8 ms                                                | 73.9 ms: 1.04x faster                                                        |
| pyflate                 | 419 ms                                                 | 403 ms: 1.04x faster                                                         |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                        |
| scimark_fft             | 325 ms                                                 | 313 ms: 1.04x faster                                                         |
| chaos                   | 68.7 ms                                                | 66.1 ms: 1.04x faster                                                        |
| deepcopy_memo           | 35.8 us                                                | 34.5 us: 1.04x faster                                                        |
| genshi_text             | 21.5 ms                                                | 20.8 ms: 1.04x faster                                                        |
| bench_thread_pool       | 817 us                                                 | 789 us: 1.04x faster                                                         |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                                        |
| logging_format          | 6.48 us                                                | 6.26 us: 1.03x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                       |
| deepcopy_reduce         | 3.02 us                                                | 2.92 us: 1.03x faster                                                        |
| hexiom                  | 6.34 ms                                                | 6.14 ms: 1.03x faster                                                        |
| nqueens                 | 83.8 ms                                                | 81.2 ms: 1.03x faster                                                        |
| crypto_pyaes            | 75.7 ms                                                | 73.7 ms: 1.03x faster                                                        |
| scimark_monte_carlo     | 68.0 ms                                                | 66.1 ms: 1.03x faster                                                        |
| deepcopy                | 341 us                                                 | 333 us: 1.03x faster                                                         |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.03x faster                                                        |
| unpack_sequence         | 44.5 ns                                                | 43.4 ns: 1.02x faster                                                        |
| spectral_norm           | 98.1 ms                                                | 95.8 ms: 1.02x faster                                                        |
| docutils                | 2.60 sec                                               | 2.54 sec: 1.02x faster                                                       |
| pprint_safe_repr        | 706 ms                                                 | 690 ms: 1.02x faster                                                         |
| regex_effbot            | 3.46 ms                                                | 3.38 ms: 1.02x faster                                                        |
| fannkuch                | 384 ms                                                 | 376 ms: 1.02x faster                                                         |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                         |
| raytrace                | 291 ms                                                 | 285 ms: 1.02x faster                                                         |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                        |
| telco                   | 6.43 ms                                                | 6.32 ms: 1.02x faster                                                        |
| tornado_http            | 96.5 ms                                                | 95.1 ms: 1.02x faster                                                        |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                                         |
| coverage                | 99.3 ms                                                | 98.1 ms: 1.01x faster                                                        |
| dulwich_log             | 64.0 ms                                                | 63.4 ms: 1.01x faster                                                        |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                                        |
| mako                    | 9.83 ms                                                | 9.75 ms: 1.01x faster                                                        |
| pickle_dict             | 31.2 us                                                | 30.9 us: 1.01x faster                                                        |
| pickle_list             | 4.14 us                                                | 4.12 us: 1.01x faster                                                        |
| pidigits                | 197 ms                                                 | 197 ms: 1.00x slower                                                         |
| django_template         | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                        |
| thrift                  | 760 us                                                 | 766 us: 1.01x slower                                                         |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                                       |
| meteor_contest          | 104 ms                                                 | 106 ms: 1.01x slower                                                         |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                                        |
| async_tree_cpu_io_mixed | 736 ms                                                 | 750 ms: 1.02x slower                                                         |
| chameleon               | 6.38 ms                                                | 6.51 ms: 1.02x slower                                                        |
| gc_traversal            | 3.82 ms                                                | 3.91 ms: 1.02x slower                                                        |
| nbody                   | 90.0 ms                                                | 93.0 ms: 1.03x slower                                                        |
| unpickle                | 13.3 us                                                | 13.7 us: 1.03x slower                                                        |
| regex_dna               | 203 ms                                                 | 211 ms: 1.04x slower                                                         |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                                        |
| xml_etree_process       | 53.7 ms                                                | 55.9 ms: 1.04x slower                                                        |
| python_startup          | 8.58 ms                                                | 8.96 ms: 1.04x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                | 1.72 ms: 1.04x slower                                                        |
| mdp                     | 2.63 sec                                               | 2.75 sec: 1.05x slower                                                       |
| sqlglot_parse           | 1.36 ms                                                | 1.43 ms: 1.05x slower                                                        |
| xml_etree_generate      | 75.9 ms                                                | 80.6 ms: 1.06x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.49 ms: 1.08x slower                                                        |
| async_generators        | 356 ms                                                 | 410 ms: 1.15x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (7): sqlalchemy_declarative, async_tree_none, djangocms, unpickle_list, regex_v8, bench_mp_pool, async_tree_memoization
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, pylint
