
# Results vs. 3.11.0

- fork: brandtbucher
- ref: scan_small_dicts
- machine: linux-x86_64
- commit hash: ba16621
- commit date: 2022-12-17
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                     |
| chameleon      | 6.38 ms                                                | 6.26 ms: 1.02x faster                                                    |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                   |
| html5lib       | 64.8 ms                                                | 59.6 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.0 ms: 1.07x faster                                                    |
| pidigits       | 197 ms                                                 | 198 ms: 1.00x slower                                                     |
| nbody          | 90.0 ms                                                | 94.1 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.05x faster                                                     |
| regex_v8       | 22.2 ms                                                | 21.3 ms: 1.05x faster                                                    |
| regex_effbot   | 3.46 ms                                                | 3.50 ms: 1.01x slower                                                    |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.39 ms: 1.32x faster                                                    |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                                     |
| pickle_pure_python   | 308 us                                                 | 281 us: 1.10x faster                                                     |
| json_loads           | 26.1 us                                                | 24.0 us: 1.09x faster                                                    |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.09x faster                                                     |
| unpickle             | 13.3 us                                                | 13.0 us: 1.02x faster                                                    |
| pickle_list          | 4.14 us                                                | 4.10 us: 1.01x faster                                                    |
| xml_etree_process    | 53.7 ms                                                | 53.2 ms: 1.01x faster                                                    |
| pickle_dict          | 31.2 us                                                | 30.9 us: 1.01x faster                                                    |
| xml_etree_generate   | 75.9 ms                                                | 76.2 ms: 1.00x slower                                                    |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                                    |
| unpickle_list        | 4.99 us                                                | 5.09 us: 1.02x slower                                                    |
| xml_etree_iterparse  | 104 ms                                                 | 107 ms: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.51 ms: 1.01x faster                                                    |
| python_startup_no_site | 6.04 ms                                                | 6.09 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.9 ms: 1.10x faster                                                    |
| genshi_text     | 21.5 ms                                                | 20.3 ms: 1.06x faster                                                    |
| mako            | 9.83 ms                                                | 9.42 ms: 1.04x faster                                                    |
| django_template | 32.3 ms                                                | 32.2 ms: 1.00x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.39 ms: 1.32x faster                                                    |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                                     |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.01 ms: 1.14x faster                                                    |
| deltablue               | 3.66 ms                                                | 3.22 ms: 1.13x faster                                                    |
| richards                | 46.1 ms                                                | 42.0 ms: 1.10x faster                                                    |
| genshi_xml              | 51.4 ms                                                | 46.9 ms: 1.10x faster                                                    |
| pycparser               | 1.19 sec                                               | 1.08 sec: 1.10x faster                                                   |
| pickle_pure_python      | 308 us                                                 | 281 us: 1.10x faster                                                     |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.10x faster                                                     |
| json_loads              | 26.1 us                                                | 24.0 us: 1.09x faster                                                    |
| html5lib                | 64.8 ms                                                | 59.6 ms: 1.09x faster                                                    |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.09x faster                                                     |
| nqueens                 | 83.8 ms                                                | 77.4 ms: 1.08x faster                                                    |
| deepcopy_memo           | 35.8 us                                                | 33.2 us: 1.08x faster                                                    |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.07x faster                                                   |
| float                   | 76.8 ms                                                | 72.0 ms: 1.07x faster                                                    |
| logging_silent          | 98.0 ns                                                | 91.9 ns: 1.07x faster                                                    |
| hexiom                  | 6.34 ms                                                | 5.96 ms: 1.06x faster                                                    |
| genshi_text             | 21.5 ms                                                | 20.3 ms: 1.06x faster                                                    |
| deepcopy                | 341 us                                                 | 323 us: 1.06x faster                                                     |
| unpack_sequence         | 44.5 ns                                                | 42.1 ns: 1.06x faster                                                    |
| pprint_safe_repr        | 706 ms                                                 | 669 ms: 1.05x faster                                                     |
| logging_simple          | 6.02 us                                                | 5.72 us: 1.05x faster                                                    |
| bench_thread_pool       | 817 us                                                 | 777 us: 1.05x faster                                                     |
| scimark_fft             | 325 ms                                                 | 310 ms: 1.05x faster                                                     |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                     |
| sqlglot_optimize        | 52.7 ms                                                | 50.3 ms: 1.05x faster                                                    |
| regex_compile           | 136 ms                                                 | 130 ms: 1.05x faster                                                     |
| regex_v8                | 22.2 ms                                                | 21.3 ms: 1.05x faster                                                    |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.05x faster                                                     |
| mako                    | 9.83 ms                                                | 9.42 ms: 1.04x faster                                                    |
| raytrace                | 291 ms                                                 | 280 ms: 1.04x faster                                                     |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                     |
| deepcopy_reduce         | 3.02 us                                                | 2.90 us: 1.04x faster                                                    |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                   |
| logging_format          | 6.48 us                                                | 6.26 us: 1.03x faster                                                    |
| pathlib                 | 18.1 ms                                                | 17.5 ms: 1.03x faster                                                    |
| coroutines              | 26.2 ms                                                | 25.3 ms: 1.03x faster                                                    |
| spectral_norm           | 98.1 ms                                                | 95.1 ms: 1.03x faster                                                    |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                    |
| sympy_str               | 291 ms                                                 | 282 ms: 1.03x faster                                                     |
| scimark_lu              | 108 ms                                                 | 105 ms: 1.03x faster                                                     |
| scimark_monte_carlo     | 68.0 ms                                                | 66.0 ms: 1.03x faster                                                    |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                     |
| pyflate                 | 419 ms                                                 | 407 ms: 1.03x faster                                                     |
| mdp                     | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                   |
| dulwich_log             | 64.0 ms                                                | 62.3 ms: 1.03x faster                                                    |
| async_generators        | 356 ms                                                 | 348 ms: 1.02x faster                                                     |
| chaos                   | 68.7 ms                                                | 67.3 ms: 1.02x faster                                                    |
| fannkuch                | 384 ms                                                 | 377 ms: 1.02x faster                                                     |
| chameleon               | 6.38 ms                                                | 6.26 ms: 1.02x faster                                                    |
| unpickle                | 13.3 us                                                | 13.0 us: 1.02x faster                                                    |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                                     |
| json                    | 4.87 ms                                                | 4.81 ms: 1.01x faster                                                    |
| pickle_list             | 4.14 us                                                | 4.10 us: 1.01x faster                                                    |
| xml_etree_process       | 53.7 ms                                                | 53.2 ms: 1.01x faster                                                    |
| thrift                  | 760 us                                                 | 754 us: 1.01x faster                                                     |
| python_startup          | 8.58 ms                                                | 8.51 ms: 1.01x faster                                                    |
| pickle_dict             | 31.2 us                                                | 30.9 us: 1.01x faster                                                    |
| django_template         | 32.3 ms                                                | 32.2 ms: 1.00x faster                                                    |
| crypto_pyaes            | 75.7 ms                                                | 75.5 ms: 1.00x faster                                                    |
| xml_etree_generate      | 75.9 ms                                                | 76.2 ms: 1.00x slower                                                    |
| pidigits                | 197 ms                                                 | 198 ms: 1.00x slower                                                     |
| python_startup_no_site  | 6.04 ms                                                | 6.09 ms: 1.01x slower                                                    |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                   |
| async_tree_none         | 526 ms                                                 | 533 ms: 1.01x slower                                                     |
| coverage                | 99.3 ms                                                | 101 ms: 1.01x slower                                                     |
| regex_effbot            | 3.46 ms                                                | 3.50 ms: 1.01x slower                                                    |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                                    |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                                     |
| unpickle_list           | 4.99 us                                                | 5.09 us: 1.02x slower                                                    |
| sqlglot_transpile       | 1.65 ms                                                | 1.69 ms: 1.02x slower                                                    |
| xml_etree_iterparse     | 104 ms                                                 | 107 ms: 1.02x slower                                                     |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed | 736 ms                                                 | 758 ms: 1.03x slower                                                     |
| sqlite_synth            | 2.48 us                                                | 2.56 us: 1.03x slower                                                    |
| nbody                   | 90.0 ms                                                | 94.1 ms: 1.05x slower                                                    |
| generators              | 73.5 ms                                                | 77.0 ms: 1.05x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (5): telco, bench_mp_pool, djangocms, meteor_contest, async_tree_memoization
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221217-3.12.0a3+-ba16621/bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621.json: mypy
