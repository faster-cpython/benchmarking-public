
# Results vs. 3.11.0

- fork: faster-cpython
- ref: no_deep_freeze
- machine: linux-x86_64
- commit hash: 76326f3
- commit date: 2023-03-16
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                       |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                     |
| html5lib       | 64.8 ms                                                | 59.2 ms: 1.10x faster                                                      |
| tornado_http   | 96.5 ms                                                | 90.9 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.7 ms: 1.04x faster                                                      |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                       |
| nbody          | 90.0 ms                                                | 88.2 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 133 ms: 1.03x faster                                                       |
| regex_dna      | 203 ms                                                 | 204 ms: 1.01x slower                                                       |
| regex_v8       | 22.2 ms                                                | 25.6 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.62 ms: 1.29x faster                                                      |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                                       |
| pickle_pure_python   | 308 us                                                 | 282 us: 1.09x faster                                                       |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                      |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 99.7 ms: 1.04x faster                                                      |
| pickle_dict          | 31.2 us                                                | 30.0 us: 1.04x faster                                                      |
| pickle_list          | 4.14 us                                                | 4.21 us: 1.02x slower                                                      |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                      |
| xml_etree_process    | 53.7 ms                                                | 56.4 ms: 1.05x slower                                                      |
| unpickle_list        | 4.99 us                                                | 5.32 us: 1.07x slower                                                      |
| xml_etree_generate   | 75.9 ms                                                | 81.8 ms: 1.08x slower                                                      |
| unpickle             | 13.3 us                                                | 14.5 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.04 ms                                                | 6.48 ms: 1.07x slower                                                      |
| python_startup         | 8.58 ms                                                | 9.51 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.7 ms: 1.08x faster                                                      |
| genshi_text     | 21.5 ms                                                | 21.2 ms: 1.02x faster                                                      |
| django_template | 32.3 ms                                                | 33.1 ms: 1.02x slower                                                      |
| mako            | 9.83 ms                                                | 10.2 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.9 ms: 2.45x faster                                                      |
| asyncio_tcp             | 883 ms                                                 | 507 ms: 1.74x faster                                                       |
| json_dumps              | 12.4 ms                                                | 9.62 ms: 1.29x faster                                                      |
| coroutines              | 26.2 ms                                                | 22.2 ms: 1.18x faster                                                      |
| deltablue               | 3.66 ms                                                | 3.15 ms: 1.16x faster                                                      |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                                       |
| mdp                     | 2.63 sec                                               | 2.40 sec: 1.10x faster                                                     |
| html5lib                | 64.8 ms                                                | 59.2 ms: 1.10x faster                                                      |
| pickle_pure_python      | 308 us                                                 | 282 us: 1.09x faster                                                       |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                      |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                       |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.09x faster                                                       |
| coverage                | 99.3 ms                                                | 91.6 ms: 1.08x faster                                                      |
| spectral_norm           | 98.1 ms                                                | 90.6 ms: 1.08x faster                                                      |
| richards                | 46.1 ms                                                | 42.6 ms: 1.08x faster                                                      |
| genshi_xml              | 51.4 ms                                                | 47.7 ms: 1.08x faster                                                      |
| json                    | 4.87 ms                                                | 4.54 ms: 1.07x faster                                                      |
| scimark_fft             | 325 ms                                                 | 304 ms: 1.07x faster                                                       |
| deepcopy_memo           | 35.8 us                                                | 33.7 us: 1.06x faster                                                      |
| go                      | 140 ms                                                 | 132 ms: 1.06x faster                                                       |
| tornado_http            | 96.5 ms                                                | 90.9 ms: 1.06x faster                                                      |
| logging_simple          | 6.02 us                                                | 5.69 us: 1.06x faster                                                      |
| aiohttp                 | 1.05 ms                                                | 996 us: 1.05x faster                                                       |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.37 ms: 1.05x faster                                                      |
| logging_silent          | 98.0 ns                                                | 93.4 ns: 1.05x faster                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 99.7 ms: 1.04x faster                                                      |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                     |
| float                   | 76.8 ms                                                | 73.7 ms: 1.04x faster                                                      |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                                      |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                       |
| hexiom                  | 6.34 ms                                                | 6.10 ms: 1.04x faster                                                      |
| deepcopy                | 341 us                                                 | 328 us: 1.04x faster                                                       |
| gc_traversal            | 3.82 ms                                                | 3.68 ms: 1.04x faster                                                      |
| pickle_dict             | 31.2 us                                                | 30.0 us: 1.04x faster                                                      |
| unpack_sequence         | 44.5 ns                                                | 42.8 ns: 1.04x faster                                                      |
| fannkuch                | 384 ms                                                 | 371 ms: 1.04x faster                                                       |
| raytrace                | 291 ms                                                 | 282 ms: 1.03x faster                                                       |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                     |
| bench_thread_pool       | 817 us                                                 | 791 us: 1.03x faster                                                       |
| nqueens                 | 83.8 ms                                                | 81.1 ms: 1.03x faster                                                      |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                       |
| async_tree_memoization  | 624 ms                                                 | 606 ms: 1.03x faster                                                       |
| chaos                   | 68.7 ms                                                | 66.7 ms: 1.03x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                      |
| regex_compile           | 136 ms                                                 | 133 ms: 1.03x faster                                                       |
| pprint_safe_repr        | 706 ms                                                 | 687 ms: 1.03x faster                                                       |
| dulwich_log             | 64.0 ms                                                | 62.3 ms: 1.03x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                       |
| sqlglot_optimize        | 52.7 ms                                                | 51.4 ms: 1.03x faster                                                      |
| sympy_str               | 291 ms                                                 | 284 ms: 1.02x faster                                                       |
| sympy_expand            | 475 ms                                                 | 464 ms: 1.02x faster                                                       |
| logging_format          | 6.48 us                                                | 6.34 us: 1.02x faster                                                      |
| nbody                   | 90.0 ms                                                | 88.2 ms: 1.02x faster                                                      |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.02x faster                                                      |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                       |
| deepcopy_reduce         | 3.02 us                                                | 2.96 us: 1.02x faster                                                      |
| genshi_text             | 21.5 ms                                                | 21.2 ms: 1.02x faster                                                      |
| crypto_pyaes            | 75.7 ms                                                | 74.4 ms: 1.02x faster                                                      |
| scimark_lu              | 108 ms                                                 | 106 ms: 1.02x faster                                                       |
| pycparser               | 1.19 sec                                               | 1.17 sec: 1.01x faster                                                     |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.01x faster                                                      |
| scimark_monte_carlo     | 68.0 ms                                                | 67.0 ms: 1.01x faster                                                      |
| regex_dna               | 203 ms                                                 | 204 ms: 1.01x slower                                                       |
| pyflate                 | 419 ms                                                 | 423 ms: 1.01x slower                                                       |
| pickle_list             | 4.14 us                                                | 4.21 us: 1.02x slower                                                      |
| thrift                  | 760 us                                                 | 772 us: 1.02x slower                                                       |
| async_tree_none         | 526 ms                                                 | 535 ms: 1.02x slower                                                       |
| telco                   | 6.43 ms                                                | 6.56 ms: 1.02x slower                                                      |
| django_template         | 32.3 ms                                                | 33.1 ms: 1.02x slower                                                      |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                      |
| mako                    | 9.83 ms                                                | 10.2 ms: 1.04x slower                                                      |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                                      |
| sqlglot_parse           | 1.36 ms                                                | 1.42 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed | 736 ms                                                 | 770 ms: 1.05x slower                                                       |
| xml_etree_process       | 53.7 ms                                                | 56.4 ms: 1.05x slower                                                      |
| unpickle_list           | 4.99 us                                                | 5.32 us: 1.07x slower                                                      |
| sqlite_synth            | 2.48 us                                                | 2.65 us: 1.07x slower                                                      |
| python_startup_no_site  | 6.04 ms                                                | 6.48 ms: 1.07x slower                                                      |
| xml_etree_generate      | 75.9 ms                                                | 81.8 ms: 1.08x slower                                                      |
| unpickle                | 13.3 us                                                | 14.5 us: 1.09x slower                                                      |
| python_startup          | 8.58 ms                                                | 9.51 ms: 1.11x slower                                                      |
| regex_v8                | 22.2 ms                                                | 25.6 ms: 1.15x slower                                                      |
| async_generators        | 356 ms                                                 | 411 ms: 1.16x slower                                                       |
| dask                    | 365 ms                                                 | 503 ms: 1.38x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (9): sqlalchemy_imperative, meteor_contest, djangocms, chameleon, regex_effbot, sympy_sum, bench_mp_pool, async_tree_io, mypy2
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230316-3.12.0a6+-76326f3/bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3.json: comprehensions
