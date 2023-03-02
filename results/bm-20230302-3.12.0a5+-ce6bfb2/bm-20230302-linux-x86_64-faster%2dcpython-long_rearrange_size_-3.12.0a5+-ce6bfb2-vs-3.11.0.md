
# Results vs. 3.11.0

- fork: faster-cpython
- ref: long_rearrange_size_
- machine: linux-x86_64
- commit hash: ce6bfb2
- commit date: 2023-03-02
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.04x faster                                                             |
| chameleon      | 6.38 ms                                                | 6.43 ms: 1.01x slower                                                            |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                           |
| html5lib       | 64.8 ms                                                | 61.8 ms: 1.05x faster                                                            |
| tornado_http   | 96.5 ms                                                | 95.0 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 188 ms: 1.05x faster                                                             |
| float          | 76.8 ms                                                | 74.6 ms: 1.03x faster                                                            |
| nbody          | 90.0 ms                                                | 91.6 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.5 ms: 1.03x faster                                                            |
| regex_compile  | 136 ms                                                 | 134 ms: 1.01x faster                                                             |
| regex_dna      | 203 ms                                                 | 219 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.41 ms: 1.31x faster                                                            |
| unpickle_pure_python | 227 us                                                 | 200 us: 1.13x faster                                                             |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                            |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                             |
| pickle_pure_python   | 308 us                                                 | 285 us: 1.08x faster                                                             |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                             |
| pickle_dict          | 31.2 us                                                | 30.9 us: 1.01x faster                                                            |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                                            |
| unpickle             | 13.3 us                                                | 13.6 us: 1.03x slower                                                            |
| xml_etree_process    | 53.7 ms                                                | 55.7 ms: 1.04x slower                                                            |
| xml_etree_generate   | 75.9 ms                                                | 80.8 ms: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (2): pickle_list, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.02 ms: 1.05x slower                                                            |
| python_startup_no_site | 6.04 ms                                                | 6.53 ms: 1.08x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.2 ms: 1.07x faster                                                            |
| genshi_text     | 21.5 ms                                                | 21.2 ms: 1.02x faster                                                            |
| mako            | 9.83 ms                                                | 9.86 ms: 1.00x slower                                                            |
| django_template | 32.3 ms                                                | 32.7 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.0 ms: 2.37x faster                                                            |
| asyncio_tcp             | 883 ms                                                 | 509 ms: 1.74x faster                                                             |
| json_dumps              | 12.4 ms                                                | 9.41 ms: 1.31x faster                                                            |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                             |
| deltablue               | 3.66 ms                                                | 3.21 ms: 1.14x faster                                                            |
| unpickle_pure_python    | 227 us                                                 | 200 us: 1.13x faster                                                             |
| coroutines              | 26.2 ms                                                | 23.1 ms: 1.13x faster                                                            |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                            |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                             |
| pickle_pure_python      | 308 us                                                 | 285 us: 1.08x faster                                                             |
| fannkuch                | 384 ms                                                 | 360 ms: 1.07x faster                                                             |
| genshi_xml              | 51.4 ms                                                | 48.2 ms: 1.07x faster                                                            |
| json                    | 4.87 ms                                                | 4.57 ms: 1.07x faster                                                            |
| unpack_sequence         | 44.5 ns                                                | 41.9 ns: 1.06x faster                                                            |
| richards                | 46.1 ms                                                | 43.9 ms: 1.05x faster                                                            |
| pprint_safe_repr        | 706 ms                                                 | 672 ms: 1.05x faster                                                             |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                           |
| mdp                     | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                           |
| scimark_sor             | 115 ms                                                 | 110 ms: 1.05x faster                                                             |
| html5lib                | 64.8 ms                                                | 61.8 ms: 1.05x faster                                                            |
| pidigits                | 197 ms                                                 | 188 ms: 1.05x faster                                                             |
| logging_simple          | 6.02 us                                                | 5.78 us: 1.04x faster                                                            |
| nqueens                 | 83.8 ms                                                | 80.4 ms: 1.04x faster                                                            |
| deepcopy_memo           | 35.8 us                                                | 34.4 us: 1.04x faster                                                            |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                            |
| pycparser               | 1.19 sec                                               | 1.14 sec: 1.04x faster                                                           |
| logging_silent          | 98.0 ns                                                | 94.3 ns: 1.04x faster                                                            |
| coverage                | 99.3 ms                                                | 95.7 ms: 1.04x faster                                                            |
| 2to3                    | 259 ms                                                 | 251 ms: 1.04x faster                                                             |
| regex_v8                | 22.2 ms                                                | 21.5 ms: 1.03x faster                                                            |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                             |
| sympy_expand            | 475 ms                                                 | 460 ms: 1.03x faster                                                             |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                             |
| deepcopy                | 341 us                                                 | 331 us: 1.03x faster                                                             |
| float                   | 76.8 ms                                                | 74.6 ms: 1.03x faster                                                            |
| sqlglot_optimize        | 52.7 ms                                                | 51.2 ms: 1.03x faster                                                            |
| logging_format          | 6.48 us                                                | 6.30 us: 1.03x faster                                                            |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                            |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.02x faster                                                            |
| pyflate                 | 419 ms                                                 | 409 ms: 1.02x faster                                                             |
| bench_thread_pool       | 817 us                                                 | 800 us: 1.02x faster                                                             |
| hexiom                  | 6.34 ms                                                | 6.21 ms: 1.02x faster                                                            |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                           |
| sympy_str               | 291 ms                                                 | 286 ms: 1.02x faster                                                             |
| sympy_integrate         | 21.0 ms                                                | 20.6 ms: 1.02x faster                                                            |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.02x faster                                                            |
| genshi_text             | 21.5 ms                                                | 21.2 ms: 1.02x faster                                                            |
| crypto_pyaes            | 75.7 ms                                                | 74.5 ms: 1.02x faster                                                            |
| tornado_http            | 96.5 ms                                                | 95.0 ms: 1.02x faster                                                            |
| chaos                   | 68.7 ms                                                | 67.6 ms: 1.02x faster                                                            |
| regex_compile           | 136 ms                                                 | 134 ms: 1.01x faster                                                             |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                                             |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                             |
| scimark_monte_carlo     | 68.0 ms                                                | 67.1 ms: 1.01x faster                                                            |
| pickle_dict             | 31.2 us                                                | 30.9 us: 1.01x faster                                                            |
| raytrace                | 291 ms                                                 | 289 ms: 1.01x faster                                                             |
| scimark_fft             | 325 ms                                                 | 324 ms: 1.01x faster                                                             |
| mako                    | 9.83 ms                                                | 9.86 ms: 1.00x slower                                                            |
| chameleon               | 6.38 ms                                                | 6.43 ms: 1.01x slower                                                            |
| sympy_sum               | 166 ms                                                 | 167 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed | 736 ms                                                 | 744 ms: 1.01x slower                                                             |
| telco                   | 6.43 ms                                                | 6.50 ms: 1.01x slower                                                            |
| django_template         | 32.3 ms                                                | 32.7 ms: 1.01x slower                                                            |
| nbody                   | 90.0 ms                                                | 91.6 ms: 1.02x slower                                                            |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                                            |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.71 ms: 1.03x slower                                                            |
| thrift                  | 760 us                                                 | 781 us: 1.03x slower                                                             |
| unpickle                | 13.3 us                                                | 13.6 us: 1.03x slower                                                            |
| scimark_lu              | 108 ms                                                 | 111 ms: 1.03x slower                                                             |
| xml_etree_process       | 53.7 ms                                                | 55.7 ms: 1.04x slower                                                            |
| sqlglot_transpile       | 1.65 ms                                                | 1.73 ms: 1.05x slower                                                            |
| python_startup          | 8.58 ms                                                | 9.02 ms: 1.05x slower                                                            |
| sqlglot_parse           | 1.36 ms                                                | 1.43 ms: 1.05x slower                                                            |
| sqlite_synth            | 2.48 us                                                | 2.62 us: 1.05x slower                                                            |
| async_tree_memoization  | 624 ms                                                 | 661 ms: 1.06x slower                                                             |
| xml_etree_generate      | 75.9 ms                                                | 80.8 ms: 1.07x slower                                                            |
| gc_traversal            | 3.82 ms                                                | 4.07 ms: 1.07x slower                                                            |
| regex_dna               | 203 ms                                                 | 219 ms: 1.08x slower                                                             |
| python_startup_no_site  | 6.04 ms                                                | 6.53 ms: 1.08x slower                                                            |
| async_generators        | 356 ms                                                 | 421 ms: 1.18x slower                                                             |
| dask                    | 365 ms                                                 | 505 ms: 1.38x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (12): sqlalchemy_imperative, deepcopy_reduce, regex_effbot, dulwich_log, async_tree_io, async_tree_none, sqlalchemy_declarative, djangocms, bench_mp_pool, pickle_list, unpickle_list, spectral_norm
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230302-3.12.0a5+-ce6bfb2/bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2.json: comprehensions
