
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 866c937
- commit date: 2023-02-01
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.04x faster                                                       |
| chameleon      | 6.38 ms                                                | 6.41 ms: 1.01x slower                                                      |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                     |
| html5lib       | 64.8 ms                                                | 60.1 ms: 1.08x faster                                                      |
| tornado_http   | 96.5 ms                                                | 94.5 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 74.2 ms: 1.04x faster                                                      |
| pidigits       | 197 ms                                                 | 198 ms: 1.00x slower                                                       |
| nbody          | 90.0 ms                                                | 94.9 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                                       |
| regex_v8       | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                      |
| regex_dna      | 203 ms                                                 | 217 ms: 1.07x slower                                                       |
| regex_effbot   | 3.46 ms                                                | 3.76 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.46 ms: 1.31x faster                                                      |
| unpickle_pure_python | 227 us                                                 | 200 us: 1.14x faster                                                       |
| pickle_pure_python   | 308 us                                                 | 283 us: 1.09x faster                                                       |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                       |
| json_loads           | 26.1 us                                                | 24.3 us: 1.07x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                       |
| unpickle_list        | 4.99 us                                                | 5.04 us: 1.01x slower                                                      |
| pickle_list          | 4.14 us                                                | 4.25 us: 1.03x slower                                                      |
| xml_etree_generate   | 75.9 ms                                                | 78.0 ms: 1.03x slower                                                      |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                                      |
| pickle_dict          | 31.2 us                                                | 32.4 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (2): unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.74 ms: 1.02x slower                                                      |
| python_startup_no_site | 6.04 ms                                                | 6.27 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.8 ms: 1.10x faster                                                      |
| genshi_text     | 21.5 ms                                                | 20.7 ms: 1.04x faster                                                      |
| django_template | 32.3 ms                                                | 33.0 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 497 ms: 1.78x faster                                                       |
| json_dumps              | 12.4 ms                                                | 9.46 ms: 1.31x faster                                                      |
| deltablue               | 3.66 ms                                                | 3.18 ms: 1.15x faster                                                      |
| unpickle_pure_python    | 227 us                                                 | 200 us: 1.14x faster                                                       |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.05 ms: 1.13x faster                                                      |
| richards                | 46.1 ms                                                | 41.9 ms: 1.10x faster                                                      |
| genshi_xml              | 51.4 ms                                                | 46.8 ms: 1.10x faster                                                      |
| nqueens                 | 83.8 ms                                                | 76.9 ms: 1.09x faster                                                      |
| pickle_pure_python      | 308 us                                                 | 283 us: 1.09x faster                                                       |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                       |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                       |
| sympy_str               | 291 ms                                                 | 269 ms: 1.08x faster                                                       |
| logging_silent          | 98.0 ns                                                | 90.6 ns: 1.08x faster                                                      |
| html5lib                | 64.8 ms                                                | 60.1 ms: 1.08x faster                                                      |
| json_loads              | 26.1 us                                                | 24.3 us: 1.07x faster                                                      |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                       |
| sympy_integrate         | 21.0 ms                                                | 19.6 ms: 1.07x faster                                                      |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                                       |
| hexiom                  | 6.34 ms                                                | 5.96 ms: 1.06x faster                                                      |
| fannkuch                | 384 ms                                                 | 362 ms: 1.06x faster                                                       |
| chaos                   | 68.7 ms                                                | 64.8 ms: 1.06x faster                                                      |
| scimark_fft             | 325 ms                                                 | 307 ms: 1.06x faster                                                       |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                       |
| pprint_safe_repr        | 706 ms                                                 | 670 ms: 1.05x faster                                                       |
| sympy_expand            | 475 ms                                                 | 452 ms: 1.05x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                                     |
| deepcopy                | 341 us                                                 | 326 us: 1.05x faster                                                       |
| logging_simple          | 6.02 us                                                | 5.74 us: 1.05x faster                                                      |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                                      |
| mdp                     | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                     |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                                      |
| unpack_sequence         | 44.5 ns                                                | 42.6 ns: 1.04x faster                                                      |
| deepcopy_memo           | 35.8 us                                                | 34.3 us: 1.04x faster                                                      |
| pyflate                 | 419 ms                                                 | 402 ms: 1.04x faster                                                       |
| bench_thread_pool       | 817 us                                                 | 785 us: 1.04x faster                                                       |
| deepcopy_reduce         | 3.02 us                                                | 2.90 us: 1.04x faster                                                      |
| genshi_text             | 21.5 ms                                                | 20.7 ms: 1.04x faster                                                      |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                     |
| json                    | 4.87 ms                                                | 4.69 ms: 1.04x faster                                                      |
| scimark_monte_carlo     | 68.0 ms                                                | 65.5 ms: 1.04x faster                                                      |
| 2to3                    | 259 ms                                                 | 251 ms: 1.04x faster                                                       |
| float                   | 76.8 ms                                                | 74.2 ms: 1.04x faster                                                      |
| raytrace                | 291 ms                                                 | 283 ms: 1.03x faster                                                       |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                      |
| logging_format          | 6.48 us                                                | 6.32 us: 1.02x faster                                                      |
| pycparser               | 1.19 sec                                               | 1.16 sec: 1.02x faster                                                     |
| sqlglot_optimize        | 52.7 ms                                                | 51.5 ms: 1.02x faster                                                      |
| tornado_http            | 96.5 ms                                                | 94.5 ms: 1.02x faster                                                      |
| crypto_pyaes            | 75.7 ms                                                | 74.2 ms: 1.02x faster                                                      |
| scimark_lu              | 108 ms                                                 | 106 ms: 1.02x faster                                                       |
| dulwich_log             | 64.0 ms                                                | 62.8 ms: 1.02x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                                       |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                       |
| thrift                  | 760 us                                                 | 750 us: 1.01x faster                                                       |
| spectral_norm           | 98.1 ms                                                | 96.9 ms: 1.01x faster                                                      |
| async_generators        | 356 ms                                                 | 353 ms: 1.01x faster                                                       |
| pathlib                 | 18.1 ms                                                | 18.0 ms: 1.01x faster                                                      |
| gc_traversal            | 3.82 ms                                                | 3.82 ms: 1.00x slower                                                      |
| pidigits                | 197 ms                                                 | 198 ms: 1.00x slower                                                       |
| chameleon               | 6.38 ms                                                | 6.41 ms: 1.01x slower                                                      |
| regex_v8                | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                      |
| coverage                | 99.3 ms                                                | 100 ms: 1.01x slower                                                       |
| unpickle_list           | 4.99 us                                                | 5.04 us: 1.01x slower                                                      |
| telco                   | 6.43 ms                                                | 6.55 ms: 1.02x slower                                                      |
| python_startup          | 8.58 ms                                                | 8.74 ms: 1.02x slower                                                      |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                                     |
| django_template         | 32.3 ms                                                | 33.0 ms: 1.02x slower                                                      |
| pickle_list             | 4.14 us                                                | 4.25 us: 1.03x slower                                                      |
| xml_etree_generate      | 75.9 ms                                                | 78.0 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed | 736 ms                                                 | 758 ms: 1.03x slower                                                       |
| generators              | 73.5 ms                                                | 76.0 ms: 1.03x slower                                                      |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                                      |
| python_startup_no_site  | 6.04 ms                                                | 6.27 ms: 1.04x slower                                                      |
| pickle_dict             | 31.2 us                                                | 32.4 us: 1.04x slower                                                      |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                                      |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                                      |
| sqlglot_parse           | 1.36 ms                                                | 1.42 ms: 1.04x slower                                                      |
| nbody                   | 90.0 ms                                                | 94.9 ms: 1.05x slower                                                      |
| async_tree_memoization  | 624 ms                                                 | 661 ms: 1.06x slower                                                       |
| regex_dna               | 203 ms                                                 | 217 ms: 1.07x slower                                                       |
| regex_effbot            | 3.46 ms                                                | 3.76 ms: 1.09x slower                                                      |
| dask                    | 365 ms                                                 | 501 ms: 1.37x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (8): async_tree_none, unpickle, coroutines, bench_mp_pool, xml_etree_process, mako, djangocms, meteor_contest
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230201-3.12.0a4+-866c937/bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937.json: mypy
