
# Results vs. 3.11.0

- fork: brandtbucher
- ref: scan_small_dicts
- machine: linux-x86_64
- commit hash: ba16621
- commit date: 2022-12-17
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                                     |
| chameleon      | 6.41 ms                                                | 6.26 ms: 1.02x faster                                                    |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                   |
| html5lib       | 63.2 ms                                                | 59.6 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.0 ms: 1.06x faster                                                    |
| nbody          | 95.0 ms                                                | 94.1 ms: 1.01x faster                                                    |
| pidigits       | 199 ms                                                 | 198 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 22.3 ms                                                | 21.3 ms: 1.05x faster                                                    |
| regex_compile  | 136 ms                                                 | 130 ms: 1.04x faster                                                     |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                                     |
| regex_effbot   | 3.36 ms                                                | 3.50 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.39 ms: 1.35x faster                                                    |
| unpickle_pure_python | 225 us                                                 | 197 us: 1.14x faster                                                     |
| json_loads           | 26.2 us                                                | 24.0 us: 1.09x faster                                                    |
| pickle_pure_python   | 304 us                                                 | 281 us: 1.08x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                     |
| pickle_list          | 4.17 us                                                | 4.10 us: 1.02x faster                                                    |
| pickle_dict          | 31.4 us                                                | 30.9 us: 1.02x faster                                                    |
| xml_etree_process    | 53.8 ms                                                | 53.2 ms: 1.01x faster                                                    |
| unpickle_list        | 4.95 us                                                | 5.09 us: 1.03x slower                                                    |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                                    |
| xml_etree_iterparse  | 103 ms                                                 | 107 ms: 1.04x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (2): unpickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.51 ms: 1.02x slower                                                    |
| python_startup_no_site | 5.96 ms                                                | 6.09 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 46.9 ms: 1.11x faster                                                    |
| genshi_text     | 22.1 ms                                                | 20.3 ms: 1.09x faster                                                    |
| mako            | 9.85 ms                                                | 9.42 ms: 1.05x faster                                                    |
| django_template | 32.5 ms                                                | 32.2 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.39 ms: 1.35x faster                                                    |
| unpickle_pure_python    | 225 us                                                 | 197 us: 1.14x faster                                                     |
| deltablue               | 3.64 ms                                                | 3.22 ms: 1.13x faster                                                    |
| genshi_xml              | 52.1 ms                                                | 46.9 ms: 1.11x faster                                                    |
| richards                | 46.2 ms                                                | 42.0 ms: 1.10x faster                                                    |
| deepcopy_memo           | 36.4 us                                                | 33.2 us: 1.10x faster                                                    |
| nqueens                 | 85.0 ms                                                | 77.4 ms: 1.10x faster                                                    |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.01 ms: 1.10x faster                                                    |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.10x faster                                                     |
| json_loads              | 26.2 us                                                | 24.0 us: 1.09x faster                                                    |
| genshi_text             | 22.1 ms                                                | 20.3 ms: 1.09x faster                                                    |
| pycparser               | 1.17 sec                                               | 1.08 sec: 1.08x faster                                                   |
| pickle_pure_python      | 304 us                                                 | 281 us: 1.08x faster                                                     |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                     |
| go                      | 143 ms                                                 | 134 ms: 1.07x faster                                                     |
| logging_silent          | 98.5 ns                                                | 91.9 ns: 1.07x faster                                                    |
| hexiom                  | 6.35 ms                                                | 5.96 ms: 1.07x faster                                                    |
| deepcopy                | 344 us                                                 | 323 us: 1.06x faster                                                     |
| logging_simple          | 6.06 us                                                | 5.72 us: 1.06x faster                                                    |
| scimark_fft             | 329 ms                                                 | 310 ms: 1.06x faster                                                     |
| float                   | 76.3 ms                                                | 72.0 ms: 1.06x faster                                                    |
| html5lib                | 63.2 ms                                                | 59.6 ms: 1.06x faster                                                    |
| pprint_pformat          | 1.44 sec                                               | 1.37 sec: 1.06x faster                                                   |
| logging_format          | 6.62 us                                                | 6.26 us: 1.06x faster                                                    |
| sqlglot_optimize        | 53.0 ms                                                | 50.3 ms: 1.05x faster                                                    |
| spectral_norm           | 99.9 ms                                                | 95.1 ms: 1.05x faster                                                    |
| regex_v8                | 22.3 ms                                                | 21.3 ms: 1.05x faster                                                    |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.05x faster                                                     |
| mako                    | 9.85 ms                                                | 9.42 ms: 1.05x faster                                                    |
| regex_compile           | 136 ms                                                 | 130 ms: 1.04x faster                                                     |
| bench_thread_pool       | 810 us                                                 | 777 us: 1.04x faster                                                     |
| pathlib                 | 18.2 ms                                                | 17.5 ms: 1.04x faster                                                    |
| raytrace                | 290 ms                                                 | 280 ms: 1.04x faster                                                     |
| scimark_monte_carlo     | 68.3 ms                                                | 66.0 ms: 1.03x faster                                                    |
| sympy_expand            | 472 ms                                                 | 457 ms: 1.03x faster                                                     |
| telco                   | 6.62 ms                                                | 6.41 ms: 1.03x faster                                                    |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                   |
| pprint_safe_repr        | 691 ms                                                 | 669 ms: 1.03x faster                                                     |
| async_generators        | 359 ms                                                 | 348 ms: 1.03x faster                                                     |
| coroutines              | 26.1 ms                                                | 25.3 ms: 1.03x faster                                                    |
| unpack_sequence         | 43.4 ns                                                | 42.1 ns: 1.03x faster                                                    |
| fannkuch                | 388 ms                                                 | 377 ms: 1.03x faster                                                     |
| json                    | 4.95 ms                                                | 4.81 ms: 1.03x faster                                                    |
| sympy_integrate         | 20.9 ms                                                | 20.3 ms: 1.03x faster                                                    |
| dulwich_log             | 63.9 ms                                                | 62.3 ms: 1.03x faster                                                    |
| mdp                     | 2.62 sec                                               | 2.56 sec: 1.03x faster                                                   |
| scimark_lu              | 107 ms                                                 | 105 ms: 1.03x faster                                                     |
| pyflate                 | 417 ms                                                 | 407 ms: 1.02x faster                                                     |
| chameleon               | 6.41 ms                                                | 6.26 ms: 1.02x faster                                                    |
| deepcopy_reduce         | 2.97 us                                                | 2.90 us: 1.02x faster                                                    |
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                                     |
| chaos                   | 68.6 ms                                                | 67.3 ms: 1.02x faster                                                    |
| pickle_list             | 4.17 us                                                | 4.10 us: 1.02x faster                                                    |
| sympy_str               | 287 ms                                                 | 282 ms: 1.02x faster                                                     |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                                     |
| pickle_dict             | 31.4 us                                                | 30.9 us: 1.02x faster                                                    |
| xml_etree_process       | 53.8 ms                                                | 53.2 ms: 1.01x faster                                                    |
| nbody                   | 95.0 ms                                                | 94.1 ms: 1.01x faster                                                    |
| django_template         | 32.5 ms                                                | 32.2 ms: 1.01x faster                                                    |
| pidigits                | 199 ms                                                 | 198 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed | 752 ms                                                 | 758 ms: 1.01x slower                                                     |
| sqlglot_transpile       | 1.66 ms                                                | 1.69 ms: 1.02x slower                                                    |
| python_startup          | 8.36 ms                                                | 8.51 ms: 1.02x slower                                                    |
| python_startup_no_site  | 5.96 ms                                                | 6.09 ms: 1.02x slower                                                    |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                                     |
| sqlglot_parse           | 1.37 ms                                                | 1.40 ms: 1.02x slower                                                    |
| crypto_pyaes            | 73.9 ms                                                | 75.5 ms: 1.02x slower                                                    |
| unpickle_list           | 4.95 us                                                | 5.09 us: 1.03x slower                                                    |
| sqlite_synth            | 2.49 us                                                | 2.56 us: 1.03x slower                                                    |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                                    |
| xml_etree_iterparse     | 103 ms                                                 | 107 ms: 1.04x slower                                                     |
| regex_effbot            | 3.36 ms                                                | 3.50 ms: 1.04x slower                                                    |
| generators              | 72.2 ms                                                | 77.0 ms: 1.07x slower                                                    |
| mypy                    | 669 ms                                                 | 807 ms: 1.21x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (9): unpickle, xml_etree_generate, bench_mp_pool, coverage, meteor_contest, thrift, async_tree_io, async_tree_none, async_tree_memoization
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/mdboom/Work/builds/benchmarking/results/bm-20221217-3.12.0a3+-ba16621/bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621.json: djangocms
