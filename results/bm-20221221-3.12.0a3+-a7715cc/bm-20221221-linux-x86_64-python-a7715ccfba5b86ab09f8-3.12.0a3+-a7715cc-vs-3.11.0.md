
# Results vs. 3.11.0

- fork: python
- ref: a7715ccfba5b86ab09f8
- machine: linux-x86_64
- commit hash: a7715cc
- commit date: 2022-12-21
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.03x faster                                                   |
| docutils       | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                 |
| html5lib       | 64.8 ms                                                | 59.5 ms: 1.09x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.8 ms: 1.07x faster                                                  |
| pidigits       | 197 ms                                                 | 197 ms: 1.00x slower                                                   |
| nbody          | 90.0 ms                                                | 93.1 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.05x faster                                                   |
| regex_v8       | 22.2 ms                                                | 21.7 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.43 ms: 1.31x faster                                                  |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                                   |
| json_loads           | 26.1 us                                                | 23.6 us: 1.10x faster                                                  |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                   |
| pickle_pure_python   | 308 us                                                 | 283 us: 1.09x faster                                                   |
| pickle_list          | 4.14 us                                                | 3.98 us: 1.04x faster                                                  |
| pickle_dict          | 31.2 us                                                | 30.6 us: 1.02x faster                                                  |
| unpickle_list        | 4.99 us                                                | 4.93 us: 1.01x faster                                                  |
| xml_etree_generate   | 75.9 ms                                                | 76.5 ms: 1.01x slower                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                   |
| pickle               | 9.90 us                                                | 10.4 us: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (2): unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.43 ms: 1.02x faster                                                  |
| python_startup_no_site | 6.04 ms                                                | 6.09 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.6 ms: 1.08x faster                                                  |
| genshi_text     | 21.5 ms                                                | 20.4 ms: 1.05x faster                                                  |
| mako            | 9.83 ms                                                | 9.47 ms: 1.04x faster                                                  |
| django_template | 32.3 ms                                                | 32.5 ms: 1.00x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.43 ms: 1.31x faster                                                  |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                                   |
| deltablue               | 3.66 ms                                                | 3.20 ms: 1.14x faster                                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.10 ms: 1.12x faster                                                  |
| richards                | 46.1 ms                                                | 41.4 ms: 1.12x faster                                                  |
| json_loads              | 26.1 us                                                | 23.6 us: 1.10x faster                                                  |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                   |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.09x faster                                                   |
| html5lib                | 64.8 ms                                                | 59.5 ms: 1.09x faster                                                  |
| pickle_pure_python      | 308 us                                                 | 283 us: 1.09x faster                                                   |
| logging_silent          | 98.0 ns                                                | 90.4 ns: 1.08x faster                                                  |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                                 |
| genshi_xml              | 51.4 ms                                                | 47.6 ms: 1.08x faster                                                  |
| unpack_sequence         | 44.5 ns                                                | 41.3 ns: 1.08x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.36 sec: 1.07x faster                                                 |
| float                   | 76.8 ms                                                | 71.8 ms: 1.07x faster                                                  |
| pprint_safe_repr        | 706 ms                                                 | 661 ms: 1.07x faster                                                   |
| nqueens                 | 83.8 ms                                                | 78.5 ms: 1.07x faster                                                  |
| coroutines              | 26.2 ms                                                | 24.5 ms: 1.07x faster                                                  |
| logging_simple          | 6.02 us                                                | 5.68 us: 1.06x faster                                                  |
| fannkuch                | 384 ms                                                 | 363 ms: 1.06x faster                                                   |
| scimark_monte_carlo     | 68.0 ms                                                | 64.2 ms: 1.06x faster                                                  |
| pyflate                 | 419 ms                                                 | 396 ms: 1.06x faster                                                   |
| sympy_expand            | 475 ms                                                 | 451 ms: 1.06x faster                                                   |
| deepcopy_memo           | 35.8 us                                                | 33.9 us: 1.06x faster                                                  |
| genshi_text             | 21.5 ms                                                | 20.4 ms: 1.05x faster                                                  |
| scimark_fft             | 325 ms                                                 | 309 ms: 1.05x faster                                                   |
| sqlglot_optimize        | 52.7 ms                                                | 50.1 ms: 1.05x faster                                                  |
| hexiom                  | 6.34 ms                                                | 6.02 ms: 1.05x faster                                                  |
| json                    | 4.87 ms                                                | 4.63 ms: 1.05x faster                                                  |
| docutils                | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                 |
| regex_compile           | 136 ms                                                 | 130 ms: 1.05x faster                                                   |
| bench_thread_pool       | 817 us                                                 | 783 us: 1.04x faster                                                   |
| deepcopy                | 341 us                                                 | 328 us: 1.04x faster                                                   |
| deepcopy_reduce         | 3.02 us                                                | 2.90 us: 1.04x faster                                                  |
| logging_format          | 6.48 us                                                | 6.22 us: 1.04x faster                                                  |
| pickle_list             | 4.14 us                                                | 3.98 us: 1.04x faster                                                  |
| raytrace                | 291 ms                                                 | 280 ms: 1.04x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| sympy_str               | 291 ms                                                 | 280 ms: 1.04x faster                                                   |
| mako                    | 9.83 ms                                                | 9.47 ms: 1.04x faster                                                  |
| spectral_norm           | 98.1 ms                                                | 94.8 ms: 1.04x faster                                                  |
| mdp                     | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                 |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.03x faster                                                  |
| regex_v8                | 22.2 ms                                                | 21.7 ms: 1.03x faster                                                  |
| 2to3                    | 259 ms                                                 | 253 ms: 1.03x faster                                                   |
| thrift                  | 760 us                                                 | 741 us: 1.03x faster                                                   |
| telco                   | 6.43 ms                                                | 6.29 ms: 1.02x faster                                                  |
| dulwich_log             | 64.0 ms                                                | 62.6 ms: 1.02x faster                                                  |
| sympy_sum               | 166 ms                                                 | 162 ms: 1.02x faster                                                   |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                                   |
| pickle_dict             | 31.2 us                                                | 30.6 us: 1.02x faster                                                  |
| crypto_pyaes            | 75.7 ms                                                | 74.4 ms: 1.02x faster                                                  |
| python_startup          | 8.58 ms                                                | 8.43 ms: 1.02x faster                                                  |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| unpickle_list           | 4.99 us                                                | 4.93 us: 1.01x faster                                                  |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                                  |
| pidigits                | 197 ms                                                 | 197 ms: 1.00x slower                                                   |
| django_template         | 32.3 ms                                                | 32.5 ms: 1.00x slower                                                  |
| xml_etree_generate      | 75.9 ms                                                | 76.5 ms: 1.01x slower                                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.09 ms: 1.01x slower                                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                                 |
| async_tree_none         | 526 ms                                                 | 535 ms: 1.02x slower                                                   |
| sqlglot_transpile       | 1.65 ms                                                | 1.68 ms: 1.02x slower                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                                   |
| sqlglot_parse           | 1.36 ms                                                | 1.39 ms: 1.02x slower                                                  |
| coverage                | 99.3 ms                                                | 102 ms: 1.03x slower                                                   |
| async_tree_memoization  | 624 ms                                                 | 644 ms: 1.03x slower                                                   |
| nbody                   | 90.0 ms                                                | 93.1 ms: 1.03x slower                                                  |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 765 ms: 1.04x slower                                                   |
| pickle                  | 9.90 us                                                | 10.4 us: 1.05x slower                                                  |
| generators              | 73.5 ms                                                | 77.4 ms: 1.05x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (9): unpickle, meteor_contest, chameleon, xml_etree_process, regex_effbot, async_generators, chaos, bench_mp_pool, regex_dna
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221221-3.12.0a3+-a7715cc/bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc.json: mypy
