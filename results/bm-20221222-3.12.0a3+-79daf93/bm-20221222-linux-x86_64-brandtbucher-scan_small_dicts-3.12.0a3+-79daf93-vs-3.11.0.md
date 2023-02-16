
# Results vs. 3.11.0

- fork: brandtbucher
- ref: scan_small_dicts
- machine: linux-x86_64
- commit hash: 79daf93
- commit date: 2022-12-22
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.03x faster                                                     |
| chameleon      | 6.38 ms                                                | 6.54 ms: 1.03x slower                                                    |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                   |
| html5lib       | 64.8 ms                                                | 59.8 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.2 ms: 1.05x faster                                                    |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                                     |
| nbody          | 90.0 ms                                                | 94.7 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 131 ms: 1.04x faster                                                     |
| regex_v8       | 22.2 ms                                                | 21.9 ms: 1.01x faster                                                    |
| regex_effbot   | 3.46 ms                                                | 3.43 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.32 ms: 1.33x faster                                                    |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                     |
| pickle_pure_python   | 308 us                                                 | 278 us: 1.11x faster                                                     |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                     |
| json_loads           | 26.1 us                                                | 24.1 us: 1.08x faster                                                    |
| pickle_list          | 4.14 us                                                | 4.11 us: 1.01x faster                                                    |
| unpickle_list        | 4.99 us                                                | 5.01 us: 1.01x slower                                                    |
| xml_etree_process    | 53.7 ms                                                | 54.0 ms: 1.01x slower                                                    |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                                    |
| xml_etree_iterparse  | 104 ms                                                 | 107 ms: 1.03x slower                                                     |
| xml_etree_generate   | 75.9 ms                                                | 78.1 ms: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (2): unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.56 ms: 1.00x faster                                                    |
| python_startup_no_site | 6.04 ms                                                | 6.12 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.4 ms: 1.09x faster                                                    |
| genshi_text     | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                    |
| mako            | 9.83 ms                                                | 9.51 ms: 1.03x faster                                                    |
| django_template | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.32 ms: 1.33x faster                                                    |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                     |
| deltablue               | 3.66 ms                                                | 3.24 ms: 1.13x faster                                                    |
| pickle_pure_python      | 308 us                                                 | 278 us: 1.11x faster                                                     |
| richards                | 46.1 ms                                                | 41.9 ms: 1.10x faster                                                    |
| deepcopy_memo           | 35.8 us                                                | 32.9 us: 1.09x faster                                                    |
| genshi_xml              | 51.4 ms                                                | 47.4 ms: 1.09x faster                                                    |
| html5lib                | 64.8 ms                                                | 59.8 ms: 1.08x faster                                                    |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                     |
| json_loads              | 26.1 us                                                | 24.1 us: 1.08x faster                                                    |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                     |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                                   |
| logging_silent          | 98.0 ns                                                | 91.2 ns: 1.07x faster                                                    |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.27 ms: 1.07x faster                                                    |
| logging_simple          | 6.02 us                                                | 5.63 us: 1.07x faster                                                    |
| nqueens                 | 83.8 ms                                                | 78.4 ms: 1.07x faster                                                    |
| go                      | 140 ms                                                 | 132 ms: 1.07x faster                                                     |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                                   |
| deepcopy                | 341 us                                                 | 322 us: 1.06x faster                                                     |
| pprint_safe_repr        | 706 ms                                                 | 666 ms: 1.06x faster                                                     |
| coroutines              | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                    |
| unpack_sequence         | 44.5 ns                                                | 42.1 ns: 1.06x faster                                                    |
| pyflate                 | 419 ms                                                 | 397 ms: 1.06x faster                                                     |
| bench_thread_pool       | 817 us                                                 | 778 us: 1.05x faster                                                     |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                                     |
| fannkuch                | 384 ms                                                 | 366 ms: 1.05x faster                                                     |
| float                   | 76.8 ms                                                | 73.2 ms: 1.05x faster                                                    |
| genshi_text             | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                    |
| raytrace                | 291 ms                                                 | 279 ms: 1.04x faster                                                     |
| regex_compile           | 136 ms                                                 | 131 ms: 1.04x faster                                                     |
| deepcopy_reduce         | 3.02 us                                                | 2.89 us: 1.04x faster                                                    |
| sqlglot_optimize        | 52.7 ms                                                | 50.6 ms: 1.04x faster                                                    |
| logging_format          | 6.48 us                                                | 6.22 us: 1.04x faster                                                    |
| hexiom                  | 6.34 ms                                                | 6.10 ms: 1.04x faster                                                    |
| mako                    | 9.83 ms                                                | 9.51 ms: 1.03x faster                                                    |
| chaos                   | 68.7 ms                                                | 66.4 ms: 1.03x faster                                                    |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                     |
| scimark_monte_carlo     | 68.0 ms                                                | 65.9 ms: 1.03x faster                                                    |
| scimark_fft             | 325 ms                                                 | 316 ms: 1.03x faster                                                     |
| telco                   | 6.43 ms                                                | 6.24 ms: 1.03x faster                                                    |
| sympy_str               | 291 ms                                                 | 283 ms: 1.03x faster                                                     |
| 2to3                    | 259 ms                                                 | 253 ms: 1.03x faster                                                     |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                    |
| spectral_norm           | 98.1 ms                                                | 95.8 ms: 1.02x faster                                                    |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                                     |
| dulwich_log             | 64.0 ms                                                | 62.5 ms: 1.02x faster                                                    |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                   |
| async_generators        | 356 ms                                                 | 349 ms: 1.02x faster                                                     |
| coverage                | 99.3 ms                                                | 97.5 ms: 1.02x faster                                                    |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                    |
| regex_v8                | 22.2 ms                                                | 21.9 ms: 1.01x faster                                                    |
| thrift                  | 760 us                                                 | 750 us: 1.01x faster                                                     |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                                     |
| sympy_sum               | 166 ms                                                 | 164 ms: 1.01x faster                                                     |
| pickle_list             | 4.14 us                                                | 4.11 us: 1.01x faster                                                    |
| regex_effbot            | 3.46 ms                                                | 3.43 ms: 1.01x faster                                                    |
| python_startup          | 8.58 ms                                                | 8.56 ms: 1.00x faster                                                    |
| crypto_pyaes            | 75.7 ms                                                | 75.9 ms: 1.00x slower                                                    |
| django_template         | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                    |
| unpickle_list           | 4.99 us                                                | 5.01 us: 1.01x slower                                                    |
| xml_etree_process       | 53.7 ms                                                | 54.0 ms: 1.01x slower                                                    |
| python_startup_no_site  | 6.04 ms                                                | 6.12 ms: 1.01x slower                                                    |
| generators              | 73.5 ms                                                | 74.8 ms: 1.02x slower                                                    |
| async_tree_none         | 526 ms                                                 | 537 ms: 1.02x slower                                                     |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                                    |
| chameleon               | 6.38 ms                                                | 6.54 ms: 1.03x slower                                                    |
| async_tree_io           | 1.30 sec                                               | 1.34 sec: 1.03x slower                                                   |
| xml_etree_iterparse     | 104 ms                                                 | 107 ms: 1.03x slower                                                     |
| xml_etree_generate      | 75.9 ms                                                | 78.1 ms: 1.03x slower                                                    |
| meteor_contest          | 104 ms                                                 | 108 ms: 1.03x slower                                                     |
| mdp                     | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                   |
| json                    | 4.87 ms                                                | 5.03 ms: 1.03x slower                                                    |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                                    |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                                    |
| async_tree_memoization  | 624 ms                                                 | 651 ms: 1.04x slower                                                     |
| sqlglot_parse           | 1.36 ms                                                | 1.42 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed | 736 ms                                                 | 768 ms: 1.04x slower                                                     |
| nbody                   | 90.0 ms                                                | 94.7 ms: 1.05x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (5): unpickle, bench_mp_pool, pickle_dict, regex_dna, djangocms
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221222-3.12.0a3+-79daf93/bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93.json: mypy
