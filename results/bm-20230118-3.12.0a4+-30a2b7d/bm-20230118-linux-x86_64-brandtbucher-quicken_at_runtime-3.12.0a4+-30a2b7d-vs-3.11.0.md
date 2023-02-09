
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 30a2b7d
- commit date: 2023-01-18
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 250 ms: 1.03x faster                                                       |
| chameleon      | 6.41 ms                                                | 6.51 ms: 1.02x slower                                                      |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                     |
| html5lib       | 63.2 ms                                                | 60.5 ms: 1.04x faster                                                      |
| tornado_http   | 96.6 ms                                                | 94.9 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 71.8 ms: 1.06x faster                                                      |
| nbody          | 95.0 ms                                                | 93.5 ms: 1.02x faster                                                      |
| pidigits       | 199 ms                                                 | 197 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                                       |
| regex_v8       | 22.3 ms                                                | 22.4 ms: 1.00x slower                                                      |
| regex_dna      | 203 ms                                                 | 216 ms: 1.06x slower                                                       |
| regex_effbot   | 3.36 ms                                                | 3.68 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.43 ms: 1.34x faster                                                      |
| unpickle_pure_python | 225 us                                                 | 199 us: 1.13x faster                                                       |
| pickle_pure_python   | 304 us                                                 | 282 us: 1.08x faster                                                       |
| json_loads           | 26.2 us                                                | 24.4 us: 1.08x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 150 ms: 1.06x faster                                                       |
| pickle_list          | 4.17 us                                                | 4.11 us: 1.02x faster                                                      |
| pickle_dict          | 31.4 us                                                | 31.2 us: 1.01x faster                                                      |
| xml_etree_process    | 53.8 ms                                                | 54.2 ms: 1.01x slower                                                      |
| unpickle_list        | 4.95 us                                                | 5.01 us: 1.01x slower                                                      |
| xml_etree_generate   | 76.2 ms                                                | 78.2 ms: 1.03x slower                                                      |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                                      |
| xml_etree_iterparse  | 103 ms                                                 | 107 ms: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.71 ms: 1.04x slower                                                      |
| python_startup_no_site | 5.96 ms                                                | 6.25 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.1 ms: 1.11x faster                                                      |
| genshi_text     | 22.1 ms                                                | 20.8 ms: 1.06x faster                                                      |
| mako            | 9.85 ms                                                | 9.78 ms: 1.01x faster                                                      |
| django_template | 32.5 ms                                                | 33.0 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.43 ms: 1.34x faster                                                      |
| deltablue               | 3.64 ms                                                | 3.17 ms: 1.15x faster                                                      |
| unpickle_pure_python    | 225 us                                                 | 199 us: 1.13x faster                                                       |
| genshi_xml              | 52.1 ms                                                | 47.1 ms: 1.11x faster                                                      |
| nqueens                 | 85.0 ms                                                | 76.9 ms: 1.11x faster                                                      |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.02 ms: 1.10x faster                                                      |
| logging_silent          | 98.5 ns                                                | 90.1 ns: 1.09x faster                                                      |
| chaos                   | 68.6 ms                                                | 62.8 ms: 1.09x faster                                                      |
| fannkuch                | 388 ms                                                 | 357 ms: 1.09x faster                                                       |
| scimark_fft             | 329 ms                                                 | 304 ms: 1.08x faster                                                       |
| hexiom                  | 6.35 ms                                                | 5.87 ms: 1.08x faster                                                      |
| go                      | 143 ms                                                 | 133 ms: 1.08x faster                                                       |
| pickle_pure_python      | 304 us                                                 | 282 us: 1.08x faster                                                       |
| deepcopy_memo           | 36.4 us                                                | 33.8 us: 1.08x faster                                                      |
| json_loads              | 26.2 us                                                | 24.4 us: 1.08x faster                                                      |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                       |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.07x faster                                                       |
| sympy_str               | 287 ms                                                 | 269 ms: 1.07x faster                                                       |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                                       |
| json                    | 4.95 ms                                                | 4.64 ms: 1.07x faster                                                      |
| float                   | 76.3 ms                                                | 71.8 ms: 1.06x faster                                                      |
| genshi_text             | 22.1 ms                                                | 20.8 ms: 1.06x faster                                                      |
| sympy_integrate         | 20.9 ms                                                | 19.6 ms: 1.06x faster                                                      |
| deepcopy                | 344 us                                                 | 324 us: 1.06x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 150 ms: 1.06x faster                                                       |
| richards                | 46.2 ms                                                | 43.7 ms: 1.06x faster                                                      |
| pyflate                 | 417 ms                                                 | 396 ms: 1.05x faster                                                       |
| aiohttp                 | 1.05 ms                                                | 993 us: 1.05x faster                                                       |
| mdp                     | 2.62 sec                                               | 2.49 sec: 1.05x faster                                                     |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                      |
| coroutines              | 26.1 ms                                                | 24.8 ms: 1.05x faster                                                      |
| telco                   | 6.62 ms                                                | 6.32 ms: 1.05x faster                                                      |
| logging_simple          | 6.06 us                                                | 5.80 us: 1.05x faster                                                      |
| html5lib                | 63.2 ms                                                | 60.5 ms: 1.04x faster                                                      |
| sympy_expand            | 472 ms                                                 | 452 ms: 1.04x faster                                                       |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.04x faster                                                     |
| scimark_monte_carlo     | 68.3 ms                                                | 65.5 ms: 1.04x faster                                                      |
| sqlglot_optimize        | 53.0 ms                                                | 50.8 ms: 1.04x faster                                                      |
| raytrace                | 290 ms                                                 | 279 ms: 1.04x faster                                                       |
| bench_thread_pool       | 810 us                                                 | 780 us: 1.04x faster                                                       |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                     |
| logging_format          | 6.62 us                                                | 6.40 us: 1.03x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                       |
| 2to3                    | 257 ms                                                 | 250 ms: 1.03x faster                                                       |
| async_generators        | 359 ms                                                 | 350 ms: 1.03x faster                                                       |
| pycparser               | 1.17 sec                                               | 1.15 sec: 1.02x faster                                                     |
| pprint_safe_repr        | 691 ms                                                 | 676 ms: 1.02x faster                                                       |
| tornado_http            | 96.6 ms                                                | 94.9 ms: 1.02x faster                                                      |
| pickle_list             | 4.17 us                                                | 4.11 us: 1.02x faster                                                      |
| nbody                   | 95.0 ms                                                | 93.5 ms: 1.02x faster                                                      |
| dulwich_log             | 63.9 ms                                                | 63.0 ms: 1.02x faster                                                      |
| pidigits                | 199 ms                                                 | 197 ms: 1.01x faster                                                       |
| crypto_pyaes            | 73.9 ms                                                | 73.3 ms: 1.01x faster                                                      |
| deepcopy_reduce         | 2.97 us                                                | 2.94 us: 1.01x faster                                                      |
| pickle_dict             | 31.4 us                                                | 31.2 us: 1.01x faster                                                      |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                      |
| mako                    | 9.85 ms                                                | 9.78 ms: 1.01x faster                                                      |
| regex_v8                | 22.3 ms                                                | 22.4 ms: 1.00x slower                                                      |
| xml_etree_process       | 53.8 ms                                                | 54.2 ms: 1.01x slower                                                      |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                                     |
| unpickle_list           | 4.95 us                                                | 5.01 us: 1.01x slower                                                      |
| chameleon               | 6.41 ms                                                | 6.51 ms: 1.02x slower                                                      |
| django_template         | 32.5 ms                                                | 33.0 ms: 1.02x slower                                                      |
| coverage                | 101 ms                                                 | 102 ms: 1.02x slower                                                       |
| sqlglot_transpile       | 1.66 ms                                                | 1.69 ms: 1.02x slower                                                      |
| sqlglot_parse           | 1.37 ms                                                | 1.40 ms: 1.02x slower                                                      |
| xml_etree_generate      | 76.2 ms                                                | 78.2 ms: 1.03x slower                                                      |
| async_tree_memoization  | 625 ms                                                 | 642 ms: 1.03x slower                                                       |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.04x slower                                                      |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                                      |
| xml_etree_iterparse     | 103 ms                                                 | 107 ms: 1.04x slower                                                       |
| unpack_sequence         | 43.4 ns                                                | 45.1 ns: 1.04x slower                                                      |
| python_startup          | 8.36 ms                                                | 8.71 ms: 1.04x slower                                                      |
| generators              | 72.2 ms                                                | 75.5 ms: 1.05x slower                                                      |
| python_startup_no_site  | 5.96 ms                                                | 6.25 ms: 1.05x slower                                                      |
| meteor_contest          | 105 ms                                                 | 111 ms: 1.06x slower                                                       |
| regex_dna               | 203 ms                                                 | 216 ms: 1.06x slower                                                       |
| regex_effbot            | 3.36 ms                                                | 3.68 ms: 1.10x slower                                                      |
| mypy                    | 669 ms                                                 | 805 ms: 1.20x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (7): async_tree_none, scimark_lu, spectral_norm, unpickle, bench_mp_pool, thrift, async_tree_cpu_io_mixed
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230118-3.12.0a4+-30a2b7d/bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
