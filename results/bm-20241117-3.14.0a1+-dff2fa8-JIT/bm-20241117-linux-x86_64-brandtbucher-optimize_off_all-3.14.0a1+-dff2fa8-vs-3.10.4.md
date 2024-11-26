# Results vs. 3.10.4

- fork: brandtbucher
- ref: optimize_off_all
- machine: linux-x86_64
- commit hash: dff2fa8
- commit date: 2024-11-17
- overall geometric mean: 1.290x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 303 ms: 1.15x faster                                                     |
| docutils       | 3.30 sec                                               | 3.27 sec: 1.01x faster                                                   |
| html5lib       | 88.9 ms                                                | 68.5 ms: 1.30x faster                                                    |
| Geometric mean | (ref)                                                  | 1.14x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 343 ms: 2.12x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 430 ms: 2.02x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 882 ms: 2.00x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 592 ms: 1.72x faster                                                     |
| Geometric mean          | (ref)                                                  | 1.96x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 102 ms: 1.50x faster                                                     |
| float          | 117 ms                                                 | 81.7 ms: 1.43x faster                                                    |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.30x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 162 ms: 1.16x faster                                                     |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                    |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 229 us: 1.44x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 350 us: 1.38x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 62.2 ms: 1.27x faster                                                    |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                    |
| json_loads           | 31.2 us                                                | 26.2 us: 1.19x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 86.3 ms: 1.15x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.26x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                    |
| django_template | 48.2 ms                                                | 35.8 ms: 1.34x faster                                                    |
| genshi_text     | 31.8 ms                                                | 27.3 ms: 1.17x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 67.0 ms: 1.01x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.23x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 179 us: 3.05x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.63 ms: 2.18x faster                                                    |
| async_tree_none          | 728 ms                                                 | 343 ms: 2.12x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 430 ms: 2.02x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 882 ms: 2.00x faster                                                     |
| generators               | 80.1 ms                                                | 40.9 ms: 1.96x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 73.5 ms: 1.74x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 592 ms: 1.72x faster                                                     |
| chaos                    | 115 ms                                                 | 67.6 ms: 1.71x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 34.5 us: 1.70x faster                                                    |
| raytrace                 | 507 ms                                                 | 307 ms: 1.65x faster                                                     |
| logging_silent           | 190 ns                                                 | 116 ns: 1.63x faster                                                     |
| richards_super           | 94.7 ms                                                | 58.7 ms: 1.61x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 73.6 ms: 1.61x faster                                                    |
| scimark_sor              | 220 ms                                                 | 138 ms: 1.60x faster                                                     |
| deepcopy                 | 479 us                                                 | 303 us: 1.58x faster                                                     |
| go                       | 240 ms                                                 | 152 ms: 1.58x faster                                                     |
| djangocms                | 38.4 us                                                | 24.3 us: 1.58x faster                                                    |
| richards                 | 79.3 ms                                                | 50.2 ms: 1.58x faster                                                    |
| coroutines               | 35.1 ms                                                | 22.4 ms: 1.57x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                   |
| nbody                    | 154 ms                                                 | 102 ms: 1.50x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.46 ms: 1.49x faster                                                    |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                    |
| comprehensions           | 28.8 us                                                | 19.8 us: 1.45x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 229 us: 1.44x faster                                                     |
| logging_format           | 9.09 us                                                | 6.34 us: 1.43x faster                                                    |
| float                    | 117 ms                                                 | 81.7 ms: 1.43x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.81 us: 1.43x faster                                                    |
| pyflate                  | 716 ms                                                 | 507 ms: 1.41x faster                                                     |
| pylint                   | 551 ms                                                 | 396 ms: 1.39x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 3.01 us: 1.39x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 350 us: 1.38x faster                                                     |
| scimark_lu               | 176 ms                                                 | 128 ms: 1.38x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.88 ms: 1.37x faster                                                    |
| thrift                   | 1.07 ms                                                | 794 us: 1.35x faster                                                     |
| django_template          | 48.2 ms                                                | 35.8 ms: 1.34x faster                                                    |
| scimark_fft              | 466 ms                                                 | 347 ms: 1.34x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.88 ms: 1.33x faster                                                    |
| spectral_norm            | 170 ms                                                 | 128 ms: 1.33x faster                                                     |
| html5lib                 | 88.9 ms                                                | 68.5 ms: 1.30x faster                                                    |
| sqlalchemy_imperative    | 23.3 ms                                                | 18.1 ms: 1.29x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 62.2 ms: 1.27x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                    |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                    |
| fannkuch                 | 532 ms                                                 | 430 ms: 1.24x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.28 sec: 1.23x faster                                                   |
| hexiom                   | 10.4 ms                                                | 8.50 ms: 1.22x faster                                                    |
| json_loads               | 31.2 us                                                | 26.2 us: 1.19x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 71.1 ms: 1.19x faster                                                    |
| genshi_text              | 31.8 ms                                                | 27.3 ms: 1.17x faster                                                    |
| regex_compile            | 188 ms                                                 | 162 ms: 1.16x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 86.3 ms: 1.15x faster                                                    |
| json                     | 5.69 ms                                                | 4.95 ms: 1.15x faster                                                    |
| 2to3                     | 348 ms                                                 | 303 ms: 1.15x faster                                                     |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 126 ms: 1.14x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 153 ms: 1.12x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                     |
| nqueens                  | 106 ms                                                 | 95.0 ms: 1.11x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.64 sec: 1.08x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 916 us: 1.08x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                                    |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.07x faster                                                     |
| sympy_str                | 346 ms                                                 | 325 ms: 1.06x faster                                                     |
| sympy_expand             | 566 ms                                                 | 535 ms: 1.06x faster                                                     |
| sympy_sum                | 196 ms                                                 | 187 ms: 1.05x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 66.6 ms: 1.04x faster                                                    |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                     |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 995 ms: 1.02x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 25.3 ms: 1.02x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                     |
| docutils                 | 3.30 sec                                               | 3.27 sec: 1.01x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 67.0 ms: 1.01x slower                                                    |
| pprint_pformat           | 2.10 sec                                               | 2.14 sec: 1.02x slower                                                   |
| async_generators         | 444 ms                                                 | 462 ms: 1.04x slower                                                     |
| coverage                 | 79.4 ms                                                | 84.4 ms: 1.06x slower                                                    |
| telco                    | 7.27 ms                                                | 7.83 ms: 1.08x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 4.53 ms: 1.25x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 2.68 ms: 1.66x slower                                                    |
| bench_mp_pool            | 24.0 ms                                                | 85.8 ms: 3.57x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                             |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241117-3.14.0a1+-dff2fa8-JIT/bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.290x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 1.36x