
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
| 2to3           | 257 ms                                                 | 251 ms: 1.03x faster                                                       |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                     |
| html5lib       | 63.2 ms                                                | 60.1 ms: 1.05x faster                                                      |
| tornado_http   | 96.6 ms                                                | 94.5 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 74.2 ms: 1.03x faster                                                      |
| pidigits       | 199 ms                                                 | 198 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                       |
| regex_v8       | 22.3 ms                                                | 22.4 ms: 1.00x slower                                                      |
| regex_dna      | 203 ms                                                 | 217 ms: 1.07x slower                                                       |
| regex_effbot   | 3.36 ms                                                | 3.76 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.46 ms: 1.34x faster                                                      |
| unpickle_pure_python | 225 us                                                 | 200 us: 1.13x faster                                                       |
| json_loads           | 26.2 us                                                | 24.3 us: 1.08x faster                                                      |
| pickle_pure_python   | 304 us                                                 | 283 us: 1.07x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                       |
| unpickle_list        | 4.95 us                                                | 5.04 us: 1.02x slower                                                      |
| pickle_list          | 4.17 us                                                | 4.25 us: 1.02x slower                                                      |
| xml_etree_generate   | 76.2 ms                                                | 78.0 ms: 1.02x slower                                                      |
| pickle_dict          | 31.4 us                                                | 32.4 us: 1.03x slower                                                      |
| pickle               | 9.79 us                                                | 10.3 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_process, unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.74 ms: 1.05x slower                                                      |
| python_startup_no_site | 5.96 ms                                                | 6.27 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 46.8 ms: 1.11x faster                                                      |
| genshi_text     | 22.1 ms                                                | 20.7 ms: 1.07x faster                                                      |
| django_template | 32.5 ms                                                | 33.0 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.46 ms: 1.34x faster                                                      |
| deltablue               | 3.64 ms                                                | 3.18 ms: 1.15x faster                                                      |
| unpickle_pure_python    | 225 us                                                 | 200 us: 1.13x faster                                                       |
| genshi_xml              | 52.1 ms                                                | 46.8 ms: 1.11x faster                                                      |
| nqueens                 | 85.0 ms                                                | 76.9 ms: 1.11x faster                                                      |
| richards                | 46.2 ms                                                | 41.9 ms: 1.10x faster                                                      |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                       |
| logging_silent          | 98.5 ns                                                | 90.6 ns: 1.09x faster                                                      |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.05 ms: 1.09x faster                                                      |
| json_loads              | 26.2 us                                                | 24.3 us: 1.08x faster                                                      |
| go                      | 143 ms                                                 | 133 ms: 1.08x faster                                                       |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                                       |
| pickle_pure_python      | 304 us                                                 | 283 us: 1.07x faster                                                       |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                       |
| scimark_fft             | 329 ms                                                 | 307 ms: 1.07x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                       |
| sympy_str               | 287 ms                                                 | 269 ms: 1.07x faster                                                       |
| genshi_text             | 22.1 ms                                                | 20.7 ms: 1.07x faster                                                      |
| hexiom                  | 6.35 ms                                                | 5.96 ms: 1.07x faster                                                      |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                       |
| sympy_integrate         | 20.9 ms                                                | 19.6 ms: 1.06x faster                                                      |
| deepcopy_memo           | 36.4 us                                                | 34.3 us: 1.06x faster                                                      |
| chaos                   | 68.6 ms                                                | 64.8 ms: 1.06x faster                                                      |
| logging_simple          | 6.06 us                                                | 5.74 us: 1.06x faster                                                      |
| json                    | 4.95 ms                                                | 4.69 ms: 1.06x faster                                                      |
| deepcopy                | 344 us                                                 | 326 us: 1.06x faster                                                       |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                      |
| html5lib                | 63.2 ms                                                | 60.1 ms: 1.05x faster                                                      |
| logging_format          | 6.62 us                                                | 6.32 us: 1.05x faster                                                      |
| sympy_expand            | 472 ms                                                 | 452 ms: 1.05x faster                                                       |
| mdp                     | 2.62 sec                                               | 2.51 sec: 1.05x faster                                                     |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.04x faster                                                      |
| scimark_monte_carlo     | 68.3 ms                                                | 65.5 ms: 1.04x faster                                                      |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.04x faster                                                     |
| pyflate                 | 417 ms                                                 | 402 ms: 1.04x faster                                                       |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                     |
| bench_thread_pool       | 810 us                                                 | 785 us: 1.03x faster                                                       |
| pprint_safe_repr        | 691 ms                                                 | 670 ms: 1.03x faster                                                       |
| spectral_norm           | 99.9 ms                                                | 96.9 ms: 1.03x faster                                                      |
| float                   | 76.3 ms                                                | 74.2 ms: 1.03x faster                                                      |
| sqlglot_optimize        | 53.0 ms                                                | 51.5 ms: 1.03x faster                                                      |
| 2to3                    | 257 ms                                                 | 251 ms: 1.03x faster                                                       |
| raytrace                | 290 ms                                                 | 283 ms: 1.03x faster                                                       |
| deepcopy_reduce         | 2.97 us                                                | 2.90 us: 1.02x faster                                                      |
| tornado_http            | 96.6 ms                                                | 94.5 ms: 1.02x faster                                                      |
| unpack_sequence         | 43.4 ns                                                | 42.6 ns: 1.02x faster                                                      |
| dulwich_log             | 63.9 ms                                                | 62.8 ms: 1.02x faster                                                      |
| async_generators        | 359 ms                                                 | 353 ms: 1.02x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                       |
| scimark_lu              | 107 ms                                                 | 106 ms: 1.01x faster                                                       |
| pycparser               | 1.17 sec                                               | 1.16 sec: 1.01x faster                                                     |
| telco                   | 6.62 ms                                                | 6.55 ms: 1.01x faster                                                      |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                      |
| pidigits                | 199 ms                                                 | 198 ms: 1.01x faster                                                       |
| regex_v8                | 22.3 ms                                                | 22.4 ms: 1.00x slower                                                      |
| crypto_pyaes            | 73.9 ms                                                | 74.2 ms: 1.00x slower                                                      |
| async_tree_cpu_io_mixed | 752 ms                                                 | 758 ms: 1.01x slower                                                       |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.02x slower                                                     |
| django_template         | 32.5 ms                                                | 33.0 ms: 1.02x slower                                                      |
| unpickle_list           | 4.95 us                                                | 5.04 us: 1.02x slower                                                      |
| pickle_list             | 4.17 us                                                | 4.25 us: 1.02x slower                                                      |
| xml_etree_generate      | 76.2 ms                                                | 78.0 ms: 1.02x slower                                                      |
| pickle_dict             | 31.4 us                                                | 32.4 us: 1.03x slower                                                      |
| sqlglot_transpile       | 1.66 ms                                                | 1.71 ms: 1.03x slower                                                      |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.04x slower                                                      |
| sqlglot_parse           | 1.37 ms                                                | 1.42 ms: 1.04x slower                                                      |
| python_startup          | 8.36 ms                                                | 8.74 ms: 1.05x slower                                                      |
| pickle                  | 9.79 us                                                | 10.3 us: 1.05x slower                                                      |
| python_startup_no_site  | 5.96 ms                                                | 6.27 ms: 1.05x slower                                                      |
| generators              | 72.2 ms                                                | 76.0 ms: 1.05x slower                                                      |
| async_tree_memoization  | 625 ms                                                 | 661 ms: 1.06x slower                                                       |
| regex_dna               | 203 ms                                                 | 217 ms: 1.07x slower                                                       |
| regex_effbot            | 3.36 ms                                                | 3.76 ms: 1.12x slower                                                      |
| mypy                    | 669 ms                                                 | 807 ms: 1.21x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (12): async_tree_none, coverage, nbody, thrift, xml_etree_process, bench_mp_pool, mako, unpickle, chameleon, xml_etree_iterparse, meteor_contest, coroutines
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230201-3.12.0a4+-866c937/bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
