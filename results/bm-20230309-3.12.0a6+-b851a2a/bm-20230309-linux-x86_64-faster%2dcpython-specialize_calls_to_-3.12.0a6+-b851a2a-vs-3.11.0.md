
# Results vs. 3.11.0

- fork: faster-cpython
- ref: specialize_calls_to_
- machine: linux-x86_64
- commit hash: b851a2a
- commit date: 2023-03-09
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                             |
| chameleon      | 6.38 ms                                                | 6.67 ms: 1.05x slower                                                            |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                           |
| html5lib       | 64.8 ms                                                | 62.3 ms: 1.04x faster                                                            |
| tornado_http   | 96.5 ms                                                | 95.5 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                             |
| float          | 76.8 ms                                                | 74.1 ms: 1.04x faster                                                            |
| nbody          | 90.0 ms                                                | 94.0 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.5 ms: 1.03x faster                                                            |
| regex_effbot   | 3.46 ms                                                | 3.37 ms: 1.03x faster                                                            |
| regex_compile  | 136 ms                                                 | 134 ms: 1.01x faster                                                             |
| regex_dna      | 203 ms                                                 | 205 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.47 ms: 1.31x faster                                                            |
| unpickle_pure_python | 227 us                                                 | 200 us: 1.14x faster                                                             |
| json_loads           | 26.1 us                                                | 24.1 us: 1.08x faster                                                            |
| pickle_pure_python   | 308 us                                                 | 286 us: 1.08x faster                                                             |
| xml_etree_parse      | 160 ms                                                 | 150 ms: 1.07x faster                                                             |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.04x faster                                                             |
| pickle_dict          | 31.2 us                                                | 31.6 us: 1.01x slower                                                            |
| pickle_list          | 4.14 us                                                | 4.25 us: 1.03x slower                                                            |
| xml_etree_process    | 53.7 ms                                                | 55.9 ms: 1.04x slower                                                            |
| pickle               | 9.90 us                                                | 10.5 us: 1.06x slower                                                            |
| xml_etree_generate   | 75.9 ms                                                | 81.2 ms: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.03 ms: 1.05x slower                                                            |
| python_startup_no_site | 6.04 ms                                                | 6.54 ms: 1.08x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.2 ms: 1.07x faster                                                            |
| genshi_text     | 21.5 ms                                                | 21.7 ms: 1.01x slower                                                            |
| mako            | 9.83 ms                                                | 10.0 ms: 1.02x slower                                                            |
| django_template | 32.3 ms                                                | 33.4 ms: 1.03x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.3 ms: 2.42x faster                                                            |
| asyncio_tcp             | 883 ms                                                 | 513 ms: 1.72x faster                                                             |
| json_dumps              | 12.4 ms                                                | 9.47 ms: 1.31x faster                                                            |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                             |
| deltablue               | 3.66 ms                                                | 3.21 ms: 1.14x faster                                                            |
| unpickle_pure_python    | 227 us                                                 | 200 us: 1.14x faster                                                             |
| coroutines              | 26.2 ms                                                | 23.0 ms: 1.14x faster                                                            |
| raytrace                | 291 ms                                                 | 267 ms: 1.09x faster                                                             |
| json_loads              | 26.1 us                                                | 24.1 us: 1.08x faster                                                            |
| pickle_pure_python      | 308 us                                                 | 286 us: 1.08x faster                                                             |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                                             |
| xml_etree_parse         | 160 ms                                                 | 150 ms: 1.07x faster                                                             |
| unpack_sequence         | 44.5 ns                                                | 41.5 ns: 1.07x faster                                                            |
| genshi_xml              | 51.4 ms                                                | 48.2 ms: 1.07x faster                                                            |
| richards                | 46.1 ms                                                | 43.5 ms: 1.06x faster                                                            |
| mdp                     | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                           |
| json                    | 4.87 ms                                                | 4.62 ms: 1.05x faster                                                            |
| deepcopy_memo           | 35.8 us                                                | 34.0 us: 1.05x faster                                                            |
| chaos                   | 68.7 ms                                                | 65.4 ms: 1.05x faster                                                            |
| coverage                | 99.3 ms                                                | 95.1 ms: 1.04x faster                                                            |
| nqueens                 | 83.8 ms                                                | 80.3 ms: 1.04x faster                                                            |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                             |
| html5lib                | 64.8 ms                                                | 62.3 ms: 1.04x faster                                                            |
| logging_simple          | 6.02 us                                                | 5.79 us: 1.04x faster                                                            |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                           |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.04x faster                                                             |
| float                   | 76.8 ms                                                | 74.1 ms: 1.04x faster                                                            |
| logging_silent          | 98.0 ns                                                | 94.6 ns: 1.04x faster                                                            |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                            |
| regex_v8                | 22.2 ms                                                | 21.5 ms: 1.03x faster                                                            |
| scimark_fft             | 325 ms                                                 | 315 ms: 1.03x faster                                                             |
| bench_thread_pool       | 817 us                                                 | 790 us: 1.03x faster                                                             |
| fannkuch                | 384 ms                                                 | 373 ms: 1.03x faster                                                             |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                             |
| sqlglot_optimize        | 52.7 ms                                                | 51.2 ms: 1.03x faster                                                            |
| sympy_expand            | 475 ms                                                 | 462 ms: 1.03x faster                                                             |
| regex_effbot            | 3.46 ms                                                | 3.37 ms: 1.03x faster                                                            |
| pycparser               | 1.19 sec                                               | 1.16 sec: 1.02x faster                                                           |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                             |
| pprint_safe_repr        | 706 ms                                                 | 690 ms: 1.02x faster                                                             |
| deepcopy                | 341 us                                                 | 334 us: 1.02x faster                                                             |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.02x faster                                                            |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                           |
| logging_format          | 6.48 us                                                | 6.35 us: 1.02x faster                                                            |
| pyflate                 | 419 ms                                                 | 411 ms: 1.02x faster                                                             |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                                             |
| scimark_monte_carlo     | 68.0 ms                                                | 66.8 ms: 1.02x faster                                                            |
| sympy_integrate         | 21.0 ms                                                | 20.6 ms: 1.02x faster                                                            |
| hexiom                  | 6.34 ms                                                | 6.24 ms: 1.02x faster                                                            |
| sympy_str               | 291 ms                                                 | 287 ms: 1.02x faster                                                             |
| regex_compile           | 136 ms                                                 | 134 ms: 1.01x faster                                                             |
| crypto_pyaes            | 75.7 ms                                                | 74.7 ms: 1.01x faster                                                            |
| create_gc_cycles        | 1.52 ms                                                | 1.50 ms: 1.01x faster                                                            |
| spectral_norm           | 98.1 ms                                                | 96.9 ms: 1.01x faster                                                            |
| tornado_http            | 96.5 ms                                                | 95.5 ms: 1.01x faster                                                            |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                                             |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                                            |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                           |
| gc_traversal            | 3.82 ms                                                | 3.85 ms: 1.01x slower                                                            |
| regex_dna               | 203 ms                                                 | 205 ms: 1.01x slower                                                             |
| genshi_text             | 21.5 ms                                                | 21.7 ms: 1.01x slower                                                            |
| meteor_contest          | 104 ms                                                 | 105 ms: 1.01x slower                                                             |
| sympy_sum               | 166 ms                                                 | 168 ms: 1.01x slower                                                             |
| pickle_dict             | 31.2 us                                                | 31.6 us: 1.01x slower                                                            |
| async_tree_cpu_io_mixed | 736 ms                                                 | 747 ms: 1.01x slower                                                             |
| mako                    | 9.83 ms                                                | 10.0 ms: 1.02x slower                                                            |
| scimark_lu              | 108 ms                                                 | 110 ms: 1.02x slower                                                             |
| pickle_list             | 4.14 us                                                | 4.25 us: 1.03x slower                                                            |
| telco                   | 6.43 ms                                                | 6.61 ms: 1.03x slower                                                            |
| django_template         | 32.3 ms                                                | 33.4 ms: 1.03x slower                                                            |
| thrift                  | 760 us                                                 | 790 us: 1.04x slower                                                             |
| xml_etree_process       | 53.7 ms                                                | 55.9 ms: 1.04x slower                                                            |
| nbody                   | 90.0 ms                                                | 94.0 ms: 1.04x slower                                                            |
| chameleon               | 6.38 ms                                                | 6.67 ms: 1.05x slower                                                            |
| sqlglot_transpile       | 1.65 ms                                                | 1.73 ms: 1.05x slower                                                            |
| python_startup          | 8.58 ms                                                | 9.03 ms: 1.05x slower                                                            |
| sqlglot_parse           | 1.36 ms                                                | 1.44 ms: 1.05x slower                                                            |
| pickle                  | 9.90 us                                                | 10.5 us: 1.06x slower                                                            |
| async_tree_memoization  | 624 ms                                                 | 664 ms: 1.06x slower                                                             |
| sqlite_synth            | 2.48 us                                                | 2.64 us: 1.06x slower                                                            |
| xml_etree_generate      | 75.9 ms                                                | 81.2 ms: 1.07x slower                                                            |
| python_startup_no_site  | 6.04 ms                                                | 6.54 ms: 1.08x slower                                                            |
| async_generators        | 356 ms                                                 | 403 ms: 1.13x slower                                                             |
| dask                    | 365 ms                                                 | 513 ms: 1.40x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (9): deepcopy_reduce, async_tree_none, dulwich_log, bench_mp_pool, unpickle_list, sqlalchemy_imperative, djangocms, scimark_sparse_mat_mult, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230309-3.12.0a6+-b851a2a/bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a.json: comprehensions
