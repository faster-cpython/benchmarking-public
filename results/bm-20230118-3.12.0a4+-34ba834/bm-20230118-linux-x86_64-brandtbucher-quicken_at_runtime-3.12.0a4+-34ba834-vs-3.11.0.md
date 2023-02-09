
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 34ba834
- commit date: 2023-01-18
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 256 ms: 1.01x faster                                                       |
| chameleon      | 6.41 ms                                                | 6.56 ms: 1.02x slower                                                      |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                     |
| html5lib       | 63.2 ms                                                | 61.4 ms: 1.03x faster                                                      |
| tornado_http   | 96.6 ms                                                | 94.7 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 95.0 ms                                                | 92.5 ms: 1.03x faster                                                      |
| float          | 76.3 ms                                                | 74.3 ms: 1.03x faster                                                      |
| pidigits       | 199 ms                                                 | 198 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 22.3 ms                                                | 21.1 ms: 1.06x faster                                                      |
| regex_compile  | 136 ms                                                 | 130 ms: 1.04x faster                                                       |
| regex_dna      | 203 ms                                                 | 201 ms: 1.01x faster                                                       |
| regex_effbot   | 3.36 ms                                                | 3.44 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.55 ms: 1.33x faster                                                      |
| unpickle_pure_python | 225 us                                                 | 209 us: 1.08x faster                                                       |
| json_loads           | 26.2 us                                                | 24.4 us: 1.08x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.07x faster                                                       |
| pickle_pure_python   | 304 us                                                 | 290 us: 1.05x faster                                                       |
| pickle_list          | 4.17 us                                                | 4.02 us: 1.04x faster                                                      |
| pickle_dict          | 31.4 us                                                | 30.6 us: 1.03x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                 | 102 ms: 1.01x faster                                                       |
| xml_etree_process    | 53.8 ms                                                | 53.5 ms: 1.01x faster                                                      |
| unpickle_list        | 4.95 us                                                | 4.99 us: 1.01x slower                                                      |
| xml_etree_generate   | 76.2 ms                                                | 77.2 ms: 1.01x slower                                                      |
| pickle               | 9.79 us                                                | 10.0 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.72 ms: 1.04x slower                                                      |
| python_startup_no_site | 5.96 ms                                                | 6.25 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 48.1 ms: 1.08x faster                                                      |
| genshi_text     | 22.1 ms                                                | 20.5 ms: 1.08x faster                                                      |
| mako            | 9.85 ms                                                | 9.57 ms: 1.03x faster                                                      |
| django_template | 32.5 ms                                                | 32.7 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.55 ms: 1.33x faster                                                      |
| deltablue               | 3.64 ms                                                | 3.32 ms: 1.10x faster                                                      |
| genshi_xml              | 52.1 ms                                                | 48.1 ms: 1.08x faster                                                      |
| nqueens                 | 85.0 ms                                                | 78.7 ms: 1.08x faster                                                      |
| unpickle_pure_python    | 225 us                                                 | 209 us: 1.08x faster                                                       |
| scimark_fft             | 329 ms                                                 | 305 ms: 1.08x faster                                                       |
| genshi_text             | 22.1 ms                                                | 20.5 ms: 1.08x faster                                                      |
| json_loads              | 26.2 us                                                | 24.4 us: 1.08x faster                                                      |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.07x faster                                                       |
| deepcopy_memo           | 36.4 us                                                | 34.0 us: 1.07x faster                                                      |
| logging_silent          | 98.5 ns                                                | 92.3 ns: 1.07x faster                                                      |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                       |
| sympy_str               | 287 ms                                                 | 271 ms: 1.06x faster                                                       |
| json                    | 4.95 ms                                                | 4.67 ms: 1.06x faster                                                      |
| pycparser               | 1.17 sec                                               | 1.11 sec: 1.06x faster                                                     |
| regex_v8                | 22.3 ms                                                | 21.1 ms: 1.06x faster                                                      |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.16 ms: 1.06x faster                                                      |
| richards                | 46.2 ms                                                | 43.8 ms: 1.05x faster                                                      |
| chaos                   | 68.6 ms                                                | 65.3 ms: 1.05x faster                                                      |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.05x faster                                                     |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                      |
| spectral_norm           | 99.9 ms                                                | 95.4 ms: 1.05x faster                                                      |
| pickle_pure_python      | 304 us                                                 | 290 us: 1.05x faster                                                       |
| regex_compile           | 136 ms                                                 | 130 ms: 1.04x faster                                                       |
| deepcopy                | 344 us                                                 | 329 us: 1.04x faster                                                       |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.04x faster                                                      |
| sympy_integrate         | 20.9 ms                                                | 20.0 ms: 1.04x faster                                                      |
| sqlglot_optimize        | 53.0 ms                                                | 50.8 ms: 1.04x faster                                                      |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                     |
| pickle_list             | 4.17 us                                                | 4.02 us: 1.04x faster                                                      |
| sympy_expand            | 472 ms                                                 | 455 ms: 1.04x faster                                                       |
| hexiom                  | 6.35 ms                                                | 6.12 ms: 1.04x faster                                                      |
| logging_simple          | 6.06 us                                                | 5.85 us: 1.04x faster                                                      |
| go                      | 143 ms                                                 | 139 ms: 1.03x faster                                                       |
| logging_format          | 6.62 us                                                | 6.42 us: 1.03x faster                                                      |
| raytrace                | 290 ms                                                 | 282 ms: 1.03x faster                                                       |
| mako                    | 9.85 ms                                                | 9.57 ms: 1.03x faster                                                      |
| html5lib                | 63.2 ms                                                | 61.4 ms: 1.03x faster                                                      |
| telco                   | 6.62 ms                                                | 6.44 ms: 1.03x faster                                                      |
| pickle_dict             | 31.4 us                                                | 30.6 us: 1.03x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                       |
| nbody                   | 95.0 ms                                                | 92.5 ms: 1.03x faster                                                      |
| fannkuch                | 388 ms                                                 | 378 ms: 1.03x faster                                                       |
| float                   | 76.3 ms                                                | 74.3 ms: 1.03x faster                                                      |
| bench_thread_pool       | 810 us                                                 | 791 us: 1.02x faster                                                       |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                      |
| tornado_http            | 96.6 ms                                                | 94.7 ms: 1.02x faster                                                      |
| pprint_safe_repr        | 691 ms                                                 | 677 ms: 1.02x faster                                                       |
| dulwich_log             | 63.9 ms                                                | 62.9 ms: 1.02x faster                                                      |
| crypto_pyaes            | 73.9 ms                                                | 72.8 ms: 1.01x faster                                                      |
| thrift                  | 752 us                                                 | 741 us: 1.01x faster                                                       |
| coroutines              | 26.1 ms                                                | 25.8 ms: 1.01x faster                                                      |
| regex_dna               | 203 ms                                                 | 201 ms: 1.01x faster                                                       |
| scimark_monte_carlo     | 68.3 ms                                                | 67.6 ms: 1.01x faster                                                      |
| pidigits                | 199 ms                                                 | 198 ms: 1.01x faster                                                       |
| mdp                     | 2.62 sec                                               | 2.60 sec: 1.01x faster                                                     |
| 2to3                    | 257 ms                                                 | 256 ms: 1.01x faster                                                       |
| xml_etree_iterparse     | 103 ms                                                 | 102 ms: 1.01x faster                                                       |
| xml_etree_process       | 53.8 ms                                                | 53.5 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed | 752 ms                                                 | 756 ms: 1.01x slower                                                       |
| django_template         | 32.5 ms                                                | 32.7 ms: 1.01x slower                                                      |
| unpickle_list           | 4.95 us                                                | 4.99 us: 1.01x slower                                                      |
| meteor_contest          | 105 ms                                                 | 106 ms: 1.01x slower                                                       |
| pyflate                 | 417 ms                                                 | 421 ms: 1.01x slower                                                       |
| coverage                | 101 ms                                                 | 102 ms: 1.01x slower                                                       |
| xml_etree_generate      | 76.2 ms                                                | 77.2 ms: 1.01x slower                                                      |
| sqlglot_transpile       | 1.66 ms                                                | 1.70 ms: 1.02x slower                                                      |
| chameleon               | 6.41 ms                                                | 6.56 ms: 1.02x slower                                                      |
| regex_effbot            | 3.36 ms                                                | 3.44 ms: 1.02x slower                                                      |
| pickle                  | 9.79 us                                                | 10.0 us: 1.02x slower                                                      |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                                      |
| python_startup          | 8.36 ms                                                | 8.72 ms: 1.04x slower                                                      |
| python_startup_no_site  | 5.96 ms                                                | 6.25 ms: 1.05x slower                                                      |
| sqlite_synth            | 2.49 us                                                | 2.61 us: 1.05x slower                                                      |
| scimark_sor             | 115 ms                                                 | 121 ms: 1.05x slower                                                       |
| async_tree_memoization  | 625 ms                                                 | 659 ms: 1.06x slower                                                       |
| generators              | 72.2 ms                                                | 76.3 ms: 1.06x slower                                                      |
| mypy                    | 669 ms                                                 | 806 ms: 1.20x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (8): async_tree_none, scimark_lu, deepcopy_reduce, unpack_sequence, async_generators, bench_mp_pool, async_tree_io, unpickle
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230118-3.12.0a4+-34ba834/bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
