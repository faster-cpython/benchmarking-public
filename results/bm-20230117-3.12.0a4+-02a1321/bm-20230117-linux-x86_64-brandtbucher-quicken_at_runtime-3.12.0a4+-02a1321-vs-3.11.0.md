
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 02a1321
- commit date: 2023-01-17
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 256 ms: 1.00x faster                                                       |
| chameleon      | 6.41 ms                                                | 6.32 ms: 1.01x faster                                                      |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                     |
| html5lib       | 63.2 ms                                                | 61.5 ms: 1.03x faster                                                      |
| tornado_http   | 96.6 ms                                                | 94.4 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 76.0 ms: 1.00x faster                                                      |
| nbody          | 95.0 ms                                                | 94.0 ms: 1.01x faster                                                      |
| pidigits       | 199 ms                                                 | 193 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.05x faster                                                       |
| regex_dna      | 203 ms                                                 | 209 ms: 1.03x slower                                                       |
| regex_effbot   | 3.36 ms                                                | 3.65 ms: 1.09x slower                                                      |
| regex_v8       | 22.3 ms                                                | 21.5 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.34 ms: 1.36x faster                                                      |
| json_loads           | 26.2 us                                                | 23.9 us: 1.10x faster                                                      |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                                      |
| pickle_dict          | 31.4 us                                                | 30.8 us: 1.02x faster                                                      |
| pickle_list          | 4.17 us                                                | 4.08 us: 1.02x faster                                                      |
| pickle_pure_python   | 304 us                                                 | 293 us: 1.04x faster                                                       |
| unpickle_list        | 4.95 us                                                | 4.93 us: 1.00x faster                                                      |
| unpickle_pure_python | 225 us                                                 | 209 us: 1.08x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 151 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                 | 105 ms: 1.02x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 76.9 ms: 1.01x slower                                                      |
| xml_etree_process    | 53.8 ms                                                | 53.2 ms: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.74 ms: 1.05x slower                                                      |
| python_startup_no_site | 5.96 ms                                                | 6.27 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 32.5 ms                                                | 32.6 ms: 1.00x slower                                                      |
| genshi_text     | 22.1 ms                                                | 20.2 ms: 1.10x faster                                                      |
| genshi_xml      | 52.1 ms                                                | 46.2 ms: 1.13x faster                                                      |
| mako            | 9.85 ms                                                | 9.71 ms: 1.01x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 256 ms: 1.00x faster                                                       |
| aiohttp                 | 1.05 ms                                                | 998 us: 1.05x faster                                                       |
| async_generators        | 359 ms                                                 | 350 ms: 1.03x faster                                                       |
| async_tree_none         | 529 ms                                                 | 522 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed | 752 ms                                                 | 763 ms: 1.01x slower                                                       |
| async_tree_memoization  | 625 ms                                                 | 637 ms: 1.02x slower                                                       |
| chameleon               | 6.41 ms                                                | 6.32 ms: 1.01x faster                                                      |
| chaos                   | 68.6 ms                                                | 64.7 ms: 1.06x faster                                                      |
| bench_thread_pool       | 810 us                                                 | 782 us: 1.04x faster                                                       |
| coroutines              | 26.1 ms                                                | 25.6 ms: 1.02x faster                                                      |
| coverage                | 101 ms                                                 | 96.7 ms: 1.04x faster                                                      |
| crypto_pyaes            | 73.9 ms                                                | 72.0 ms: 1.03x faster                                                      |
| deepcopy                | 344 us                                                 | 326 us: 1.06x faster                                                       |
| deepcopy_reduce         | 2.97 us                                                | 2.95 us: 1.01x faster                                                      |
| deepcopy_memo           | 36.4 us                                                | 34.1 us: 1.07x faster                                                      |
| deltablue               | 3.64 ms                                                | 3.50 ms: 1.04x faster                                                      |
| django_template         | 32.5 ms                                                | 32.6 ms: 1.00x slower                                                      |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                     |
| dulwich_log             | 63.9 ms                                                | 62.4 ms: 1.02x faster                                                      |
| fannkuch                | 388 ms                                                 | 385 ms: 1.01x faster                                                       |
| float                   | 76.3 ms                                                | 76.0 ms: 1.00x faster                                                      |
| generators              | 72.2 ms                                                | 75.2 ms: 1.04x slower                                                      |
| genshi_text             | 22.1 ms                                                | 20.2 ms: 1.10x faster                                                      |
| genshi_xml              | 52.1 ms                                                | 46.2 ms: 1.13x faster                                                      |
| go                      | 143 ms                                                 | 139 ms: 1.03x faster                                                       |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                      |
| hexiom                  | 6.35 ms                                                | 6.00 ms: 1.06x faster                                                      |
| html5lib                | 63.2 ms                                                | 61.5 ms: 1.03x faster                                                      |
| json                    | 4.95 ms                                                | 4.56 ms: 1.09x faster                                                      |
| json_dumps              | 12.7 ms                                                | 9.34 ms: 1.36x faster                                                      |
| json_loads              | 26.2 us                                                | 23.9 us: 1.10x faster                                                      |
| logging_format          | 6.62 us                                                | 6.45 us: 1.03x faster                                                      |
| logging_silent          | 98.5 ns                                                | 89.6 ns: 1.10x faster                                                      |
| logging_simple          | 6.06 us                                                | 5.81 us: 1.04x faster                                                      |
| mako                    | 9.85 ms                                                | 9.71 ms: 1.01x faster                                                      |
| mdp                     | 2.62 sec                                               | 2.61 sec: 1.00x faster                                                     |
| meteor_contest          | 105 ms                                                 | 106 ms: 1.01x slower                                                       |
| mypy                    | 669 ms                                                 | 810 ms: 1.21x slower                                                       |
| nbody                   | 95.0 ms                                                | 94.0 ms: 1.01x faster                                                      |
| nqueens                 | 85.0 ms                                                | 78.0 ms: 1.09x faster                                                      |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                      |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                                      |
| pickle_dict             | 31.4 us                                                | 30.8 us: 1.02x faster                                                      |
| pickle_list             | 4.17 us                                                | 4.08 us: 1.02x faster                                                      |
| pickle_pure_python      | 304 us                                                 | 293 us: 1.04x faster                                                       |
| pidigits                | 199 ms                                                 | 193 ms: 1.04x faster                                                       |
| pprint_safe_repr        | 691 ms                                                 | 670 ms: 1.03x faster                                                       |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.05x faster                                                     |
| pycparser               | 1.17 sec                                               | 1.11 sec: 1.05x faster                                                     |
| pyflate                 | 417 ms                                                 | 420 ms: 1.01x slower                                                       |
| python_startup          | 8.36 ms                                                | 8.74 ms: 1.05x slower                                                      |
| python_startup_no_site  | 5.96 ms                                                | 6.27 ms: 1.05x slower                                                      |
| raytrace                | 290 ms                                                 | 299 ms: 1.03x slower                                                       |
| regex_compile           | 136 ms                                                 | 130 ms: 1.05x faster                                                       |
| regex_dna               | 203 ms                                                 | 209 ms: 1.03x slower                                                       |
| regex_effbot            | 3.36 ms                                                | 3.65 ms: 1.09x slower                                                      |
| regex_v8                | 22.3 ms                                                | 21.5 ms: 1.04x faster                                                      |
| richards                | 46.2 ms                                                | 46.6 ms: 1.01x slower                                                      |
| scimark_fft             | 329 ms                                                 | 310 ms: 1.06x faster                                                       |
| scimark_monte_carlo     | 68.3 ms                                                | 69.8 ms: 1.02x slower                                                      |
| scimark_sor             | 115 ms                                                 | 119 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.26 ms: 1.03x faster                                                      |
| spectral_norm           | 99.9 ms                                                | 97.5 ms: 1.02x faster                                                      |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                                      |
| sqlglot_transpile       | 1.66 ms                                                | 1.71 ms: 1.03x slower                                                      |
| sqlglot_optimize        | 53.0 ms                                                | 51.1 ms: 1.04x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                       |
| sqlite_synth            | 2.49 us                                                | 2.59 us: 1.04x slower                                                      |
| sympy_expand            | 472 ms                                                 | 455 ms: 1.04x faster                                                       |
| sympy_integrate         | 20.9 ms                                                | 20.0 ms: 1.05x faster                                                      |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                       |
| sympy_str               | 287 ms                                                 | 271 ms: 1.06x faster                                                       |
| telco                   | 6.62 ms                                                | 6.34 ms: 1.05x faster                                                      |
| thrift                  | 752 us                                                 | 738 us: 1.02x faster                                                       |
| tornado_http            | 96.6 ms                                                | 94.4 ms: 1.02x faster                                                      |
| unpickle_list           | 4.95 us                                                | 4.93 us: 1.00x faster                                                      |
| unpickle_pure_python    | 225 us                                                 | 209 us: 1.08x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 151 ms: 1.05x faster                                                       |
| xml_etree_iterparse     | 103 ms                                                 | 105 ms: 1.02x slower                                                       |
| xml_etree_generate      | 76.2 ms                                                | 76.9 ms: 1.01x slower                                                      |
| xml_etree_process       | 53.8 ms                                                | 53.2 ms: 1.01x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (5): async_tree_io, bench_mp_pool, scimark_lu, unpack_sequence, unpickle
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230117-3.12.0a4+-02a1321/bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
