
# Results vs. 3.11.0

- fork: faster-cpython
- ref: check_refcnt_in_bina
- machine: linux-x86_64
- commit hash: c29d369
- commit date: 2023-02-27
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.05x faster                                                             |
| chameleon      | 6.38 ms                                                | 6.51 ms: 1.02x slower                                                            |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                           |
| html5lib       | 64.8 ms                                                | 61.4 ms: 1.05x faster                                                            |
| tornado_http   | 96.5 ms                                                | 94.3 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.2 ms: 1.06x faster                                                            |
| pidigits       | 197 ms                                                 | 197 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 132 ms: 1.03x faster                                                             |
| regex_effbot   | 3.46 ms                                                | 3.36 ms: 1.03x faster                                                            |
| regex_dna      | 203 ms                                                 | 209 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.62 ms: 1.28x faster                                                            |
| unpickle_pure_python | 227 us                                                 | 196 us: 1.16x faster                                                             |
| json_loads           | 26.1 us                                                | 24.0 us: 1.09x faster                                                            |
| pickle_pure_python   | 308 us                                                 | 284 us: 1.09x faster                                                             |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                             |
| xml_etree_iterparse  | 104 ms                                                 | 98.7 ms: 1.05x faster                                                            |
| pickle_dict          | 31.2 us                                                | 30.7 us: 1.01x faster                                                            |
| unpickle_list        | 4.99 us                                                | 4.94 us: 1.01x faster                                                            |
| xml_etree_process    | 53.7 ms                                                | 54.9 ms: 1.02x slower                                                            |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                                            |
| xml_etree_generate   | 75.9 ms                                                | 79.7 ms: 1.05x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                     |

Benchmark hidden because not significant (2): pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.98 ms: 1.05x slower                                                            |
| python_startup_no_site | 6.04 ms                                                | 6.51 ms: 1.08x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.8 ms: 1.10x faster                                                            |
| genshi_text     | 21.5 ms                                                | 20.9 ms: 1.03x faster                                                            |
| mako            | 9.83 ms                                                | 9.92 ms: 1.01x slower                                                            |
| django_template | 32.3 ms                                                | 33.1 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.7 ms: 2.48x faster                                                            |
| asyncio_tcp             | 883 ms                                                 | 503 ms: 1.76x faster                                                             |
| json_dumps              | 12.4 ms                                                | 9.62 ms: 1.28x faster                                                            |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                                             |
| deltablue               | 3.66 ms                                                | 3.11 ms: 1.17x faster                                                            |
| unpickle_pure_python    | 227 us                                                 | 196 us: 1.16x faster                                                             |
| coroutines              | 26.2 ms                                                | 22.7 ms: 1.15x faster                                                            |
| richards                | 46.1 ms                                                | 40.9 ms: 1.13x faster                                                            |
| spectral_norm           | 98.1 ms                                                | 87.7 ms: 1.12x faster                                                            |
| scimark_sor             | 115 ms                                                 | 103 ms: 1.12x faster                                                             |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.17 ms: 1.10x faster                                                            |
| genshi_xml              | 51.4 ms                                                | 46.8 ms: 1.10x faster                                                            |
| json_loads              | 26.1 us                                                | 24.0 us: 1.09x faster                                                            |
| pickle_pure_python      | 308 us                                                 | 284 us: 1.09x faster                                                             |
| scimark_fft             | 325 ms                                                 | 300 ms: 1.09x faster                                                             |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                             |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                                           |
| nqueens                 | 83.8 ms                                                | 78.6 ms: 1.07x faster                                                            |
| json                    | 4.87 ms                                                | 4.57 ms: 1.06x faster                                                            |
| float                   | 76.8 ms                                                | 72.2 ms: 1.06x faster                                                            |
| fannkuch                | 384 ms                                                 | 361 ms: 1.06x faster                                                             |
| logging_silent          | 98.0 ns                                                | 92.6 ns: 1.06x faster                                                            |
| html5lib                | 64.8 ms                                                | 61.4 ms: 1.05x faster                                                            |
| xml_etree_iterparse     | 104 ms                                                 | 98.7 ms: 1.05x faster                                                            |
| raytrace                | 291 ms                                                 | 278 ms: 1.05x faster                                                             |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                             |
| 2to3                    | 259 ms                                                 | 248 ms: 1.05x faster                                                             |
| sqlglot_optimize        | 52.7 ms                                                | 50.5 ms: 1.04x faster                                                            |
| hexiom                  | 6.34 ms                                                | 6.08 ms: 1.04x faster                                                            |
| bench_thread_pool       | 817 us                                                 | 784 us: 1.04x faster                                                             |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                             |
| deepcopy_memo           | 35.8 us                                                | 34.4 us: 1.04x faster                                                            |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.04x faster                                                             |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                            |
| logging_simple          | 6.02 us                                                | 5.81 us: 1.04x faster                                                            |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                           |
| regex_compile           | 136 ms                                                 | 132 ms: 1.03x faster                                                             |
| crypto_pyaes            | 75.7 ms                                                | 73.5 ms: 1.03x faster                                                            |
| sympy_str               | 291 ms                                                 | 283 ms: 1.03x faster                                                             |
| pprint_safe_repr        | 706 ms                                                 | 685 ms: 1.03x faster                                                             |
| pyflate                 | 419 ms                                                 | 407 ms: 1.03x faster                                                             |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.03x faster                                                            |
| regex_effbot            | 3.46 ms                                                | 3.36 ms: 1.03x faster                                                            |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                            |
| genshi_text             | 21.5 ms                                                | 20.9 ms: 1.03x faster                                                            |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                           |
| deepcopy                | 341 us                                                 | 333 us: 1.03x faster                                                             |
| async_tree_io           | 1.30 sec                                               | 1.27 sec: 1.02x faster                                                           |
| tornado_http            | 96.5 ms                                                | 94.3 ms: 1.02x faster                                                            |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                            |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                            |
| logging_format          | 6.48 us                                                | 6.34 us: 1.02x faster                                                            |
| meteor_contest          | 104 ms                                                 | 102 ms: 1.02x faster                                                             |
| coverage                | 99.3 ms                                                | 97.5 ms: 1.02x faster                                                            |
| deepcopy_reduce         | 3.02 us                                                | 2.97 us: 1.02x faster                                                            |
| pickle_dict             | 31.2 us                                                | 30.7 us: 1.01x faster                                                            |
| dulwich_log             | 64.0 ms                                                | 63.2 ms: 1.01x faster                                                            |
| async_tree_none         | 526 ms                                                 | 521 ms: 1.01x faster                                                             |
| unpickle_list           | 4.99 us                                                | 4.94 us: 1.01x faster                                                            |
| mdp                     | 2.63 sec                                               | 2.61 sec: 1.01x faster                                                           |
| unpack_sequence         | 44.5 ns                                                | 44.3 ns: 1.00x faster                                                            |
| pidigits                | 197 ms                                                 | 197 ms: 1.00x slower                                                             |
| gc_traversal            | 3.82 ms                                                | 3.83 ms: 1.00x slower                                                            |
| sympy_sum               | 166 ms                                                 | 167 ms: 1.00x slower                                                             |
| mako                    | 9.83 ms                                                | 9.92 ms: 1.01x slower                                                            |
| telco                   | 6.43 ms                                                | 6.53 ms: 1.02x slower                                                            |
| chameleon               | 6.38 ms                                                | 6.51 ms: 1.02x slower                                                            |
| xml_etree_process       | 53.7 ms                                                | 54.9 ms: 1.02x slower                                                            |
| django_template         | 32.3 ms                                                | 33.1 ms: 1.02x slower                                                            |
| regex_dna               | 203 ms                                                 | 209 ms: 1.03x slower                                                             |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.03x slower                                                            |
| async_tree_memoization  | 624 ms                                                 | 645 ms: 1.03x slower                                                             |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                                            |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                                            |
| python_startup          | 8.58 ms                                                | 8.98 ms: 1.05x slower                                                            |
| xml_etree_generate      | 75.9 ms                                                | 79.7 ms: 1.05x slower                                                            |
| sqlite_synth            | 2.48 us                                                | 2.61 us: 1.05x slower                                                            |
| python_startup_no_site  | 6.04 ms                                                | 6.51 ms: 1.08x slower                                                            |
| async_generators        | 356 ms                                                 | 410 ms: 1.15x slower                                                             |
| dask                    | 365 ms                                                 | 498 ms: 1.36x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (13): djangocms, pickle_list, async_tree_cpu_io_mixed, thrift, sqlalchemy_imperative, chaos, nbody, scimark_lu, regex_v8, bench_mp_pool, scimark_monte_carlo, sqlalchemy_declarative, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
