
# Results vs. 3.11.0

- fork: brandtbucher
- ref: scan_small_dicts
- machine: linux-x86_64
- commit hash: 9e5a8e4
- commit date: 2022-12-22
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 255 ms: 1.02x faster                                                     |
| chameleon      | 6.38 ms                                                | 6.52 ms: 1.02x slower                                                    |
| docutils       | 2.60 sec                                               | 2.65 sec: 1.02x slower                                                   |
| html5lib       | 64.8 ms                                                | 60.4 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.2 ms: 1.06x faster                                                    |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                                     |
| nbody          | 90.0 ms                                                | 96.6 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                  | 1.00x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 131 ms: 1.04x faster                                                     |
| regex_v8       | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                    |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                     |
| regex_effbot   | 3.46 ms                                                | 3.58 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.43 ms: 1.31x faster                                                    |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                                     |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                    |
| pickle_pure_python   | 308 us                                                 | 285 us: 1.08x faster                                                     |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.07x faster                                                     |
| pickle_dict          | 31.2 us                                                | 30.4 us: 1.02x faster                                                    |
| pickle_list          | 4.14 us                                                | 4.09 us: 1.01x faster                                                    |
| xml_etree_process    | 53.7 ms                                                | 53.2 ms: 1.01x faster                                                    |
| xml_etree_generate   | 75.9 ms                                                | 76.3 ms: 1.01x slower                                                    |
| unpickle_list        | 4.99 us                                                | 5.03 us: 1.01x slower                                                    |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                     |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                                    |
| unpickle             | 13.3 us                                                | 13.8 us: 1.04x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.55 ms: 1.00x faster                                                    |
| python_startup_no_site | 6.04 ms                                                | 6.13 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.1 ms: 1.09x faster                                                    |
| mako            | 9.83 ms                                                | 9.37 ms: 1.05x faster                                                    |
| genshi_text     | 21.5 ms                                                | 20.6 ms: 1.04x faster                                                    |
| django_template | 32.3 ms                                                | 32.0 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.43 ms: 1.31x faster                                                    |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                                     |
| deltablue               | 3.66 ms                                                | 3.21 ms: 1.14x faster                                                    |
| scimark_sor             | 115 ms                                                 | 104 ms: 1.11x faster                                                     |
| genshi_xml              | 51.4 ms                                                | 47.1 ms: 1.09x faster                                                    |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.20 ms: 1.09x faster                                                    |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                    |
| pickle_pure_python      | 308 us                                                 | 285 us: 1.08x faster                                                     |
| logging_silent          | 98.0 ns                                                | 90.9 ns: 1.08x faster                                                    |
| deepcopy_memo           | 35.8 us                                                | 33.2 us: 1.08x faster                                                    |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.07x faster                                                     |
| html5lib                | 64.8 ms                                                | 60.4 ms: 1.07x faster                                                    |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.07x faster                                                   |
| nqueens                 | 83.8 ms                                                | 78.7 ms: 1.06x faster                                                    |
| float                   | 76.8 ms                                                | 72.2 ms: 1.06x faster                                                    |
| pprint_safe_repr        | 706 ms                                                 | 665 ms: 1.06x faster                                                     |
| logging_simple          | 6.02 us                                                | 5.68 us: 1.06x faster                                                    |
| hexiom                  | 6.34 ms                                                | 6.02 ms: 1.05x faster                                                    |
| coroutines              | 26.2 ms                                                | 24.9 ms: 1.05x faster                                                    |
| mako                    | 9.83 ms                                                | 9.37 ms: 1.05x faster                                                    |
| pyflate                 | 419 ms                                                 | 399 ms: 1.05x faster                                                     |
| raytrace                | 291 ms                                                 | 278 ms: 1.05x faster                                                     |
| bench_thread_pool       | 817 us                                                 | 780 us: 1.05x faster                                                     |
| unpack_sequence         | 44.5 ns                                                | 42.6 ns: 1.04x faster                                                    |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                                     |
| genshi_text             | 21.5 ms                                                | 20.6 ms: 1.04x faster                                                    |
| scimark_fft             | 325 ms                                                 | 312 ms: 1.04x faster                                                     |
| regex_compile           | 136 ms                                                 | 131 ms: 1.04x faster                                                     |
| pathlib                 | 18.1 ms                                                | 17.4 ms: 1.04x faster                                                    |
| sqlglot_optimize        | 52.7 ms                                                | 50.7 ms: 1.04x faster                                                    |
| deepcopy_reduce         | 3.02 us                                                | 2.91 us: 1.04x faster                                                    |
| fannkuch                | 384 ms                                                 | 371 ms: 1.04x faster                                                     |
| deepcopy                | 341 us                                                 | 329 us: 1.04x faster                                                     |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                     |
| logging_format          | 6.48 us                                                | 6.28 us: 1.03x faster                                                    |
| dulwich_log             | 64.0 ms                                                | 62.2 ms: 1.03x faster                                                    |
| pycparser               | 1.19 sec                                               | 1.16 sec: 1.03x faster                                                   |
| chaos                   | 68.7 ms                                                | 67.0 ms: 1.03x faster                                                    |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                                     |
| pickle_dict             | 31.2 us                                                | 30.4 us: 1.02x faster                                                    |
| sympy_str               | 291 ms                                                 | 285 ms: 1.02x faster                                                     |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                    |
| 2to3                    | 259 ms                                                 | 255 ms: 1.02x faster                                                     |
| telco                   | 6.43 ms                                                | 6.31 ms: 1.02x faster                                                    |
| pickle_list             | 4.14 us                                                | 4.09 us: 1.01x faster                                                    |
| async_generators        | 356 ms                                                 | 352 ms: 1.01x faster                                                     |
| richards                | 46.1 ms                                                | 45.6 ms: 1.01x faster                                                    |
| spectral_norm           | 98.1 ms                                                | 97.1 ms: 1.01x faster                                                    |
| django_template         | 32.3 ms                                                | 32.0 ms: 1.01x faster                                                    |
| xml_etree_process       | 53.7 ms                                                | 53.2 ms: 1.01x faster                                                    |
| python_startup          | 8.58 ms                                                | 8.55 ms: 1.00x faster                                                    |
| sympy_sum               | 166 ms                                                 | 166 ms: 1.00x slower                                                     |
| xml_etree_generate      | 75.9 ms                                                | 76.3 ms: 1.01x slower                                                    |
| regex_v8                | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                    |
| unpickle_list           | 4.99 us                                                | 5.03 us: 1.01x slower                                                    |
| meteor_contest          | 104 ms                                                 | 106 ms: 1.01x slower                                                     |
| python_startup_no_site  | 6.04 ms                                                | 6.13 ms: 1.02x slower                                                    |
| docutils                | 2.60 sec                                               | 2.65 sec: 1.02x slower                                                   |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                                     |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                                    |
| chameleon               | 6.38 ms                                                | 6.52 ms: 1.02x slower                                                    |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                                   |
| async_tree_none         | 526 ms                                                 | 541 ms: 1.03x slower                                                     |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                     |
| regex_effbot            | 3.46 ms                                                | 3.58 ms: 1.04x slower                                                    |
| unpickle                | 13.3 us                                                | 13.8 us: 1.04x slower                                                    |
| mdp                     | 2.63 sec                                               | 2.73 sec: 1.04x slower                                                   |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                                    |
| generators              | 73.5 ms                                                | 76.8 ms: 1.05x slower                                                    |
| async_tree_cpu_io_mixed | 736 ms                                                 | 769 ms: 1.05x slower                                                     |
| coverage                | 99.3 ms                                                | 104 ms: 1.05x slower                                                     |
| sqlglot_transpile       | 1.65 ms                                                | 1.73 ms: 1.05x slower                                                    |
| sqlglot_parse           | 1.36 ms                                                | 1.44 ms: 1.06x slower                                                    |
| json                    | 4.87 ms                                                | 5.17 ms: 1.06x slower                                                    |
| nbody                   | 90.0 ms                                                | 96.6 ms: 1.07x slower                                                    |
| async_tree_memoization  | 624 ms                                                 | 683 ms: 1.09x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                             |

Benchmark hidden because not significant (7): scimark_monte_carlo, bench_mp_pool, scimark_lu, crypto_pyaes, go, djangocms, thrift
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221222-3.12.0a3+-9e5a8e4/bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4.json: mypy
