
# Results vs. 3.11.0

- fork: faster-cpython
- ref: restrict_for_iter_sp
- machine: linux-x86_64
- commit hash: fb5f321
- commit date: 2023-02-17
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 247 ms: 1.05x faster                                                             |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                           |
| html5lib       | 64.8 ms                                                | 61.2 ms: 1.06x faster                                                            |
| tornado_http   | 96.5 ms                                                | 94.8 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.7 ms: 1.04x faster                                                            |
| pidigits       | 197 ms                                                 | 198 ms: 1.00x slower                                                             |
| nbody          | 90.0 ms                                                | 95.5 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 132 ms: 1.03x faster                                                             |
| regex_dna      | 203 ms                                                 | 199 ms: 1.02x faster                                                             |
| regex_v8       | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                            |
| regex_effbot   | 3.46 ms                                                | 3.65 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.50 ms: 1.30x faster                                                            |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                                             |
| pickle_pure_python   | 308 us                                                 | 281 us: 1.10x faster                                                             |
| json_loads           | 26.1 us                                                | 24.0 us: 1.09x faster                                                            |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                             |
| xml_etree_iterparse  | 104 ms                                                 | 99.7 ms: 1.04x faster                                                            |
| pickle_list          | 4.14 us                                                | 4.01 us: 1.03x faster                                                            |
| pickle_dict          | 31.2 us                                                | 30.2 us: 1.03x faster                                                            |
| pickle               | 9.90 us                                                | 9.98 us: 1.01x slower                                                            |
| unpickle_list        | 4.99 us                                                | 5.04 us: 1.01x slower                                                            |
| xml_etree_process    | 53.7 ms                                                | 55.7 ms: 1.04x slower                                                            |
| xml_etree_generate   | 75.9 ms                                                | 81.2 ms: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                     |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.92 ms: 1.04x slower                                                            |
| python_startup_no_site | 6.04 ms                                                | 6.47 ms: 1.07x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.4 ms: 1.06x faster                                                            |
| genshi_text     | 21.5 ms                                                | 21.2 ms: 1.02x faster                                                            |
| mako            | 9.83 ms                                                | 9.89 ms: 1.01x slower                                                            |
| django_template | 32.3 ms                                                | 33.0 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.6 ms: 2.40x faster                                                            |
| asyncio_tcp             | 883 ms                                                 | 504 ms: 1.75x faster                                                             |
| json_dumps              | 12.4 ms                                                | 9.50 ms: 1.30x faster                                                            |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                                             |
| coroutines              | 26.2 ms                                                | 22.1 ms: 1.18x faster                                                            |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                                             |
| deltablue               | 3.66 ms                                                | 3.19 ms: 1.15x faster                                                            |
| pickle_pure_python      | 308 us                                                 | 281 us: 1.10x faster                                                             |
| richards                | 46.1 ms                                                | 42.2 ms: 1.09x faster                                                            |
| json_loads              | 26.1 us                                                | 24.0 us: 1.09x faster                                                            |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                                           |
| gc_traversal            | 3.82 ms                                                | 3.53 ms: 1.08x faster                                                            |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                             |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                                             |
| sympy_str               | 291 ms                                                 | 273 ms: 1.07x faster                                                             |
| genshi_xml              | 51.4 ms                                                | 48.4 ms: 1.06x faster                                                            |
| unpack_sequence         | 44.5 ns                                                | 41.9 ns: 1.06x faster                                                            |
| fannkuch                | 384 ms                                                 | 362 ms: 1.06x faster                                                             |
| html5lib                | 64.8 ms                                                | 61.2 ms: 1.06x faster                                                            |
| json                    | 4.87 ms                                                | 4.60 ms: 1.06x faster                                                            |
| logging_simple          | 6.02 us                                                | 5.74 us: 1.05x faster                                                            |
| 2to3                    | 259 ms                                                 | 247 ms: 1.05x faster                                                             |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                             |
| sympy_integrate         | 21.0 ms                                                | 20.0 ms: 1.05x faster                                                            |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                             |
| xml_etree_iterparse     | 104 ms                                                 | 99.7 ms: 1.04x faster                                                            |
| spectral_norm           | 98.1 ms                                                | 94.1 ms: 1.04x faster                                                            |
| pyflate                 | 419 ms                                                 | 402 ms: 1.04x faster                                                             |
| float                   | 76.8 ms                                                | 73.7 ms: 1.04x faster                                                            |
| sympy_sum               | 166 ms                                                 | 159 ms: 1.04x faster                                                             |
| pprint_safe_repr        | 706 ms                                                 | 680 ms: 1.04x faster                                                             |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                            |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.04x faster                                                           |
| scimark_fft             | 325 ms                                                 | 314 ms: 1.04x faster                                                             |
| deepcopy_memo           | 35.8 us                                                | 34.6 us: 1.03x faster                                                            |
| pickle_list             | 4.14 us                                                | 4.01 us: 1.03x faster                                                            |
| sqlglot_optimize        | 52.7 ms                                                | 51.1 ms: 1.03x faster                                                            |
| bench_thread_pool       | 817 us                                                 | 791 us: 1.03x faster                                                             |
| pickle_dict             | 31.2 us                                                | 30.2 us: 1.03x faster                                                            |
| regex_compile           | 136 ms                                                 | 132 ms: 1.03x faster                                                             |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                           |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                             |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.03x faster                                                            |
| deepcopy_reduce         | 3.02 us                                                | 2.94 us: 1.03x faster                                                            |
| deepcopy                | 341 us                                                 | 333 us: 1.03x faster                                                             |
| nqueens                 | 83.8 ms                                                | 81.7 ms: 1.03x faster                                                            |
| logging_silent          | 98.0 ns                                                | 95.7 ns: 1.02x faster                                                            |
| regex_dna               | 203 ms                                                 | 199 ms: 1.02x faster                                                             |
| crypto_pyaes            | 75.7 ms                                                | 74.2 ms: 1.02x faster                                                            |
| dulwich_log             | 64.0 ms                                                | 62.8 ms: 1.02x faster                                                            |
| gunicorn                | 1.12 ms                                                | 1.10 ms: 1.02x faster                                                            |
| regex_v8                | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                            |
| tornado_http            | 96.5 ms                                                | 94.8 ms: 1.02x faster                                                            |
| logging_format          | 6.48 us                                                | 6.37 us: 1.02x faster                                                            |
| genshi_text             | 21.5 ms                                                | 21.2 ms: 1.02x faster                                                            |
| coverage                | 99.3 ms                                                | 97.9 ms: 1.01x faster                                                            |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                                             |
| scimark_monte_carlo     | 68.0 ms                                                | 67.1 ms: 1.01x faster                                                            |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                                             |
| hexiom                  | 6.34 ms                                                | 6.27 ms: 1.01x faster                                                            |
| chaos                   | 68.7 ms                                                | 68.0 ms: 1.01x faster                                                            |
| pidigits                | 197 ms                                                 | 198 ms: 1.00x slower                                                             |
| mako                    | 9.83 ms                                                | 9.89 ms: 1.01x slower                                                            |
| pickle                  | 9.90 us                                                | 9.98 us: 1.01x slower                                                            |
| unpickle_list           | 4.99 us                                                | 5.04 us: 1.01x slower                                                            |
| mdp                     | 2.63 sec                                               | 2.66 sec: 1.01x slower                                                           |
| thrift                  | 760 us                                                 | 769 us: 1.01x slower                                                             |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                                           |
| scimark_lu              | 108 ms                                                 | 110 ms: 1.02x slower                                                             |
| django_template         | 32.3 ms                                                | 33.0 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed | 736 ms                                                 | 752 ms: 1.02x slower                                                             |
| telco                   | 6.43 ms                                                | 6.58 ms: 1.02x slower                                                            |
| xml_etree_process       | 53.7 ms                                                | 55.7 ms: 1.04x slower                                                            |
| python_startup          | 8.58 ms                                                | 8.92 ms: 1.04x slower                                                            |
| sqlglot_transpile       | 1.65 ms                                                | 1.73 ms: 1.05x slower                                                            |
| regex_effbot            | 3.46 ms                                                | 3.65 ms: 1.05x slower                                                            |
| sqlglot_parse           | 1.36 ms                                                | 1.44 ms: 1.06x slower                                                            |
| nbody                   | 90.0 ms                                                | 95.5 ms: 1.06x slower                                                            |
| xml_etree_generate      | 75.9 ms                                                | 81.2 ms: 1.07x slower                                                            |
| python_startup_no_site  | 6.04 ms                                                | 6.47 ms: 1.07x slower                                                            |
| sqlite_synth            | 2.48 us                                                | 2.66 us: 1.07x slower                                                            |
| async_tree_memoization  | 624 ms                                                 | 677 ms: 1.08x slower                                                             |
| async_generators        | 356 ms                                                 | 410 ms: 1.15x slower                                                             |
| dask                    | 365 ms                                                 | 502 ms: 1.37x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (9): djangocms, sqlalchemy_imperative, raytrace, bench_mp_pool, chameleon, scimark_sparse_mat_mult, pathlib, async_tree_none, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
